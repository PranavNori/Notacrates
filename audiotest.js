let mediaRecorder;
let chunks = [];

const recordButton = document.getElementById('recordButton');
const stopButton = document.getElementById('stopButton');
const saveButton = document.getElementById('saveButton');

recordButton.addEventListener('click', startRecording);
stopButton.addEventListener('click', stopRecording);
saveButton.addEventListener('click', saveRecording);

async function startRecording() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(stream);
        mediaRecorder.ondataavailable = (e) => {
            chunks.push(e.data);
        };
        mediaRecorder.onstop = () => {
            const blob = new Blob(chunks, { 'type': 'audio/wav' });
            const url = URL.createObjectURL(blob);
            const audio = new Audio(url);
            document.body.appendChild(audio);
        };
        mediaRecorder.start();
        recordButton.disabled = true;
        stopButton.disabled = false;
    } catch (err) {
        console.error('Error accessing microphone:', err);
    }
}

function stopRecording() {
    mediaRecorder.stop();
    recordButton.disabled = false;
    stopButton.disabled = true;
    saveButton.disabled = false;
}

function saveRecording() {
    const blob = new Blob(chunks, { 'type': 'audio/wav' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    document.body.appendChild(a);
    a.style = 'display: none';
    a.href = url;
    a.download = 'recording.wav';
    a.click();
    window.URL.revokeObjectURL(url);
}
