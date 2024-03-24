from flask import Flask, request, jsonify
from openai import OpenAI
import os
from dotenv import load_dotenv
from NoteTaker import summarize_transcript

load_dotenv()
client = OpenAI()

app = Flask(__name__)

@app.route('/summarize', methods=['POST'])
def summarize():

    print("if you see this, your code works")
    # Receive audio content from the request
    final_transcription = request.form['text']

    # # Process audio content with OpenAI's audio transcription service
    # transcriptions = []
    # chunk_counter = 0

    # # Split audio content into chunks
    # chunk_size = 5 * 1024 * 1024  # 5 MB (adjust as needed)
    # while chunk_counter * chunk_size < len(audio_content):
    #     chunk_start = chunk_counter * chunk_size
    #     chunk_end = min((chunk_counter + 1) * chunk_size, len(audio_content))
    #     chunk = audio_content[chunk_start:chunk_end]

    #     # Create temporary file for the chunk
    #     filename = f"temp_chunk_{chunk_counter}.wav"
    #     with open(filename, "wb") as f:
    #         f.write(chunk)

    #     # Transcribe the chunk
    #     with open(filename, "rb") as f:
    #         transcription = client.audio.transcriptions.create(
    #             file=f,
    #             model="whisper-1", 
    #             response_format="text"
    #         )
    #         transcriptions.append(transcription)

    #     # Clean up temporary file
    #     os.remove(filename)

    #     chunk_counter += 1

    # # Concatenate transcriptions
    # final_transcription = "".join(transcriptions)
    final_transcription = summarize_transcript(final_transcription)
    return final_transcription

if __name__ == '__main__':
    app.run(debug=True)
