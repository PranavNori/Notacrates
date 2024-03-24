from pydub import AudioSegment
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()

audio = AudioSegment.from_wav("060123-John.Willinsky-The.Economics.of.Knowledge.as.a.Public.Good.wav")

file_stats = os.stat("060123-John.Willinsky-The.Economics.of.Knowledge.as.a.Public.Good.wav")

print(file_stats)

size = file_stats.st_size / (1024 * 1024)
cuts = int(size/25)+1
print(size)
print(cuts)
chunk_length_ms = int(len(audio)/cuts)
print(len(audio)/1000)
print(chunk_length_ms/1000)


chunks = [audio[i:i+chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]
if len(chunks[-1]) <= 100:
    chunks[-2] = chunks[-2]+chunks[-1]
    chunks.pop(-1)
transcriptions = []

# for i, chunk in enumerate(chunks):
#     chunk.export(f"temp_chunk_{i}.wav", format="wav")
#     transcription = client.audio.transcriptions.create(
#         file=open(f"temp_chunk_{i}.wav", "rb"),
#         model="whisper-1", 
#         response_format="text"
#     )

#     transcriptions.append(transcription)

# final_transcription = "".join(transcriptions)

for i, chunk in enumerate(chunks):
    filename = f"temp_chunk_{i}.wav"
    chunk.export(filename, format="wav")
    with open(filename, "rb") as file:
        transcription = client.audio.transcriptions.create(
            file=file,
            model="whisper-1", 
            response_format="text"
        )
    transcriptions.append(transcription)
    os.remove(filename)  # Make sure this is outside the 'with' block

final_transcription = "".join(transcriptions)

with open("transcription.txt", "w") as f:
    f.write(final_transcription)

with open("transcription.txt", "rb") as f:  # Read as binary
    content_bytes = f.read()

# Decode with 'ignore' to skip invalid UTF-8 byte sequences
cleaned_content = content_bytes.decode('utf-8', 'ignore')

with open("transcription.txt", "w", encoding="utf-8") as f:
    f.write(cleaned_content)

# for i, chunk in enumerate(chunks):
#     os.remove(f"temp_chunk_{i}.wav")

