from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload-recording', methods=['POST'])
def upload_recording():
    recording_data = request.data  # Get the recording data from the request body

    # Save the recording to a file
    with open('saved_recording.wav', 'wb') as f:
        f.write(recording_data)

    return jsonify({'message': 'Recording saved successfully'})

if __name__ == '__main__':
    app.run(debug=True)
