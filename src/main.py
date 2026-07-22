import sounddevice as sd
import wavio as wv
import numpy as np
import queue
import os
import threading
import multiprocessing as mp
import whisper
from pydub import AudioSegment
from text_edit import edit
from deepmultilingualpunctuation import PunctuationModel
import argostranslate.package
import argostranslate.translate

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

'''
from_code = "en"
to_code = "ja"

# Download and install Argos Translate package
argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()
package_to_install = next(
    filter(
        lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
    )
)
argostranslate.package.install_from_path(package_to_install.download())
'''

model = whisper.load_model("turbo")
punct_model = PunctuationModel()

transcript = ""
previous_text = ""

def transcriber():
    global chunk_number, model, transcript, previous_text
    pointer = 3

    while True:
        text = ""

        if chunk_number >= 3 and pointer < chunk_number:
            # Prep audio chunk for transcribing
            print(f"Thread: {chunk_number - 2}, {chunk_number - 1}, {chunk_number}")
            segemnt1 = AudioSegment.from_file(file = f"../chunks/chunk{pointer - 2}.wav", format = "wav")
            segment2 = AudioSegment.from_file(file = f"../chunks/chunk{pointer - 1}.wav", format = "wav")
            segment3 = AudioSegment.from_file(file = f"../chunks/chunk{pointer}.wav", format = "wav")
            
            final = segemnt1 + segment2 + segment3
            final.export("../chunks/tchunk.wav",format="wav")
                
            #Check if audio chunk is silent to avoid hallucination
            audio = AudioSegment.from_file("../chunks/tchunk.wav")
            average_level = audio.dBFS
            if average_level > -50:
                result = model.transcribe("../chunks/tchunk.wav", language="en", word_timestamps=False, condition_on_previous_text=False)
                text = result["text"].replace("?", "").replace("!", "").replace(".", "").replace(",", "").lower().lstrip() + " "
                print(average_level)

            if text != "":
                if previous_text == "":
                    print(text)
                    transcript += text
                else:
                    if previous_text != text:
                        print(f"previous_text: {previous_text}, text: {text}")
                        transcript = edit(transcript, text)
            previous_text = text
            
            pointer += 1
            print(transcript)
        text = ""

def translator():
    global transcript
    punct_transcript = ""

    pointer = 0
    end_pointer = 0

    while True:
        if end_pointer < len(transcript):
            end_pointer = len(transcript)
            block = transcript[pointer:end_pointer]
            punctuated = punct_model.restore_punctuation(block)

            count = punctuated.count(".") + punctuated.count("?")
            if count >= 2:
                #print(argostranslate.translate.translate(block))
                sentence = ""

                for letter in range(len(block)):
                    if block[letter] != "." and block[letter] != "?":
                        sentence += block[letter]
                    else:
                        sentence += block[letter]
                        pointer += letter
                        break
                punct_transcript += sentence + " "
            else:
                print(punct_transcript + punctuated)
                #print(argostranslate.translate.translate(block))



            

if __name__ == "__main__":
    process1 = mp.Process(target=transcriber)
    process1.start()
    print(f'Process created: {process1.name}')
    process2 = mp.Process(target=translator)
    process2.start()
    print(f'Process created: {process2.name}')

    # Open and run the input stream
    try:
        with sd.InputStream(samplerate=44100, channels=1, callback=audio_callback):
            print("Recording... Press Ctrl+C to stop.")
            

            while True:
                data = audio_queue.get()

                buffer.append(data)
                buffer_samples += len(data)

                if buffer_samples >= SAMPLES_PER_CHUNK:
                    # Combine buffered arrays
                    audio = np.vstack(buffer)

                    # First 1-second chunk
                    chunk = audio[:SAMPLES_PER_CHUNK]

                    filename = f"../chunks/chunk{chunk_number}.wav"

                    wv.write(
                        str(filename),
                        chunk,
                        SAMPLE_RATE,
                        sampwidth=2  # 16-bit audio
                    )

                    silence = AudioSegment.from_file(filename)

                    if silence.dBFS <= -50:
                        os.remove(filename)
                    else:
                        print(f"Saved {filename}")
                        print(f"Main: {chunk_number}")

                        chunk_number += 1

                    # Keep any leftover samples
                    leftover = audio[SAMPLES_PER_CHUNK:]
                    buffer = [leftover] if len(leftover) else []
                    buffer_samples = len(leftover)
    except KeyboardInterrupt:
        process1.join()
        process2.join()
        print(f"\nRecording stopped.\n{transcript}")


            
