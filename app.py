from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_audio', methods=['POST'])
def process_audio():
    try:
        if 'audio' not in request.files:
            return jsonify({'result': 'No audio file provided'})

        audio_file = request.files['audio']

        if audio_file.filename == '':
            return jsonify({'result': 'No selected file'})

        if audio_file:
            # Save the uploaded file to a temporary location
            filename = os.path.join(app.config['UPLOAD_FOLDER'], audio_file.filename)
            audio_file.save(filename)

            # Clean up: delete the temporary file
            os.remove(filename)

            return jsonify({'result': result})

    except Exception as e:
        return jsonify({'result': f'Error: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)