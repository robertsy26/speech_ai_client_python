from pydub import AudioSegment
import os
from pathlib import Path


final = AudioSegment.from_file(file = os.path.join("chunks", "chunk1.wav"), format = "wav")

path = Path('\chunks')
file_count = len(os.listdir("chunks"))
print(f"File Count: {file_count}")

for num in range(2, file_count + 1):
    final += AudioSegment.from_file(file = os.path.join("chunks", f"chunk{num}.wav"), format = "wav")
    print(f"Added Chunk {num}")

final.export("recording.wav", format="wav")


'''
sound1 = AudioSegment.from_file(file = os.path.join("chunks", "chunk1.wav"), format = "wav")
sound2 = AudioSegment.from_file(file = os.path.join("chunks", "chunk2.wav"), format = "wav")
sound3 = AudioSegment.from_file(file = os.path.join("chunks", "chunk3.wav"), format = "wav")
sound4 = AudioSegment.from_file(file = os.path.join("chunks", "chunk4.wav"), format = "wav")
sound5 = AudioSegment.from_file(file = os.path.join("chunks", "chunk5.wav"), format = "wav")

final1 = sound1.append(sound2)
final2 = final1.append(sound3)
final3 = final2.append(sound4)
final4 = final3.append(sound5)

final4.export("recording.wav",format="wav")
'''