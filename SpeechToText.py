from pydub import AudioSegment
from openai import OpenAI
client = OpenAI()

song = AudioSegment.from_wav("never_gonna_give_you_up.wav")
audioLength = song.duration_seconds 


transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file, 
  response_format="text"
)


print(transcription.text)