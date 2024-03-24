from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from pydub import AudioSegment
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

client = OpenAI()

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the post request has the file part
    if 'file' not in request.files:
        return jsonify(error="No file part"), 400

    file = request.files['file']

    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        return jsonify(error="No selected file"), 400

    # At this point, you have the file object and can do further processing
    # For example, save the file to a desired location, process it, etc.

    # Return a success response
    return jsonify(success=True)


@app.route('/process_audio', methods=['POST'])
def process_audio():
    # Check if the post request has the file part
    if 'audio' not in request.files:
        return jsonify(error="No file part"), 400
    file = request.files['audio']
    if file.filename == '':
        return jsonify(error="No selected file"), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join('/tmp', filename)
    file.save(filepath)

    audio = AudioSegment.from_wav(filepath)

    # Your existing logic to split the audio, transcribe it, and combine transcriptions
    # Simplified for brevity - replace with your actual transcription logic

    # Here's a placeholder for the transcription result
    final_transcription = "This is a test transcription."

    # Cleanup: remove the temporary file
    os.remove(filepath)

    # Return the transcription result
    return jsonify(transcription=final_transcription)

if __name__ == '__main__':
    app.run(debug=True)
