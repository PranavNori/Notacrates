# app.py
from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

app = Flask(__name__)

# Configure Google Cloud Speech-to-Text
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/frogchewer/Documents/GitHub/Notacrates/forward-karma-418214-fce356846d0a.json'

#

# HTML template for the app
@app.route('/')
def index():
    return render_template('index.html')

# Flask route to handle recording and transcription
@app.route('/record', methods=['POST'])
def record():
    # Check if the request contains audio data
    if 'audio_data' not in request.files:
        return jsonify({'error': 'No audio data found'})

    audio_data = request.files['audio_data']
    audio_data.save('recorded_audio.wav')  # Save audio file

    # Transcribe the audio using Google Cloud Speech-to-Text
    client = speech.SpeechClient()
    with open('recorded_audio.wav', 'rb') as audio_file:
        content = audio_file.read()
    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code='en-US'
    )
    response = client.recognize(config=config, audio=audio)

    transcription = ''
    for result in response.results:
        transcription += result.alternatives[0].transcript

    # Delete the recorded audio file
    os.remove('recorded_audio.wav')

    return jsonify({'transcription': transcription})

if __name__ == '__main__':
    app.run(debug=True)
