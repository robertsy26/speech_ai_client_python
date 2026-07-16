import sounddevice as sd
import wavio as wv
import numpy as np
import queue
import os
import threading
import whisper
from pydub import AudioSegment
import time
from text_edit import edit

# Create a queue to hold audio chunks safely
audio_queue = queue.Queue()

SAMPLE_RATE = 44100
CHANNELS = 1
CHUNK_SECONDS = 1
SAMPLES_PER_CHUNK = SAMPLE_RATE * CHUNK_SECONDS

# Define the callback function
def audio_callback(indata, frames, time, status):
    if status:
        print(f"Status Error: {status}")
    # Put a copy of the incoming NumPy array into the queue
    audio_queue.put(indata.copy())

buffer = []
buffer_samples = 0
chunk_number = 1

model = whisper.load_model("turbo")

transcript = ""
previous_text = ""
start_time = time.perf_counter()

def transcriber():
    global chunk_number, model, transcript, start_time, previous_text
    pointer = 3
    text = ""

    while True:
        if chunk_number >= 3 and pointer < chunk_number:
            # Prep audio chunk for transcribing
            print(f"Thread: {chunk_number - 2}, {chunk_number - 1}, {chunk_number}")
            segemnt1 = AudioSegment.from_file(file = os.path.join("chunks", f"chunk{pointer - 2}.wav"), format = "wav")
            segment2 = AudioSegment.from_file(file = os.path.join("chunks", f"chunk{pointer - 1}.wav"), format = "wav")
            segment3 = AudioSegment.from_file(file = os.path.join("chunks", f"chunk{pointer}.wav"), format = "wav")
            
            final = segemnt1 + segment2 + segment3
            final.export("tchunk.wav",format="wav")
                
            #Check if audio chunk is silent to avoid hallucination
            audio = AudioSegment.from_file("tchunk.wav")
            average_level = audio.dBFS
            if average_level <= -50:
                print("")
            else:
                result = model.transcribe("tchunk.wav", language="en", word_timestamps=False, condition_on_previous_text=False)
                text = result["text"].replace("?", "").replace("!", "").replace(".", "").lower().lstrip() + " "
                print(average_level)
                print(result["text"])
                file = open("transcript.txt", "a")
                file.write(result["text"] + "\n")

            elapsed = time.perf_counter() - start_time

            
            if previous_text == "" or elapsed >= 1.5:
                transcript += text
                start_time = time.perf_counter()
            else:
                if previous_text != text:
                    transcript = edit(transcript, text)
                    previous_text = text
            
            pointer += 1
            print(transcript)
        text = ""
            

# Open and run the input stream
try:
    with sd.InputStream(samplerate=44100, channels=1, callback=audio_callback):
        print("Recording... Press Ctrl+C to stop.")
        thread1 = threading.Thread(target=transcriber, daemon=True)
        thread1.start()
        print(f'Thread created: {thread1.name}')
        while True:
            data = audio_queue.get()

            buffer.append(data)
            buffer_samples += len(data)

            if buffer_samples >= SAMPLES_PER_CHUNK:
                # Combine buffered arrays
                audio = np.vstack(buffer)

                # First 1-second chunk
                chunk = audio[:SAMPLES_PER_CHUNK]

                filename = os.path.join("chunks", f"chunk{chunk_number}.wav")

                wv.write(
                    str(filename),
                    chunk,
                    SAMPLE_RATE,
                    sampwidth=2  # 16-bit audio
                )

                print(f"Saved {filename}")
                print(f"Main: {chunk_number}")

                chunk_number += 1

                # Keep any leftover samples
                leftover = audio[SAMPLES_PER_CHUNK:]
                buffer = [leftover] if len(leftover) else []
                buffer_samples = len(leftover)
except KeyboardInterrupt:
    print(f"\nRecording stopped.\n{transcript}")


            
