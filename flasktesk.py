from flask import Flask, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()
# Configure OpenAI API key

@app.route('/process_audio', methods=['POST'])
def process_audio():
    audio_file = request.files['audio']
    # Save the uploaded audio file to server
    audio_path = 'uploaded_audio.wav'
    audio_file.save(audio_path)

    # Process and transcribe the audio using the OpenAI API
    with open(audio_path, 'rb') as f:
        audio_data = f.read()

    response = OpenAI.Speech.create(
        audio=audio_data,
        model="davinci",
        max_tokens=100
    )
    transcription = response['text']
    return jsonify({'transcription': transcription})

if __name__ == '__main__':
    app.run(debug=True)
