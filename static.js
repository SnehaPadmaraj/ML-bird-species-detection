function processAudio() {
    const input = document.getElementById('audioInput');
    const outputDiv = document.getElementById('output');

    const file = input.files[0];
    if (!file) {
        alert('Please select an audio file.');
        return;
    }

    const formData = new FormData();
    formData.append('audio', file);

    fetch('/process_audio', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        outputDiv.innerText = `Model Output: ${data.result}`;
    })
    .catch(error => {
        console.error('Error:', error);
        outputDiv.innerText = 'Error occurred during processing.';
    });
}