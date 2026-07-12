from pydub import AudioSegment

# Load the audio file (works for wav, mp3, ogg, flac, etc.)
audio = AudioSegment.from_file("tchunk.wav")

# Get average audio level in dBFS
average_level = audio.dBFS

# Get peak audio level in dBFS
peak_level = audio.max_dBFS

print(f"Average Audio Level: {average_level:.2f} dBFS")
print(f"Peak Audio Level: {peak_level:.2f} dBFS\n")

if average_level >= -80 and average_level <= -60:
    print("Audio is silent")
else:
    print("Audio is not silent")