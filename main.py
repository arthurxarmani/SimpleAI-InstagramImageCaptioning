from flask import Flask, request, jsonify
from PIL import Image
import io
# Assume 'generate_caption' is a function that takes an image and returns a caption
from caption_generator import generate_caption

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        image = Image.open(io.BytesIO(file.read()))
        caption = generate_caption(image)
        return jsonify({'caption': caption})

if __name__ == '__main__':
    app.run(debug=True)