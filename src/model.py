import whisper

model = whisper.load_model("turbo")
result = model.transcribe("short_audio.flac")

f = open("transcript.txt", "a")
f.write(result["text"])