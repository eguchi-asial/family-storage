from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)
UPLOAD_FOLDER = '/mnt/share'

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    files = request.files.getlist('file')
    for file in files:
        if file.filename == '':
            return 'No selected file'
        if not allowed_file(file.filename):
            return 'File type not allowed'
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return 'Files saved successfully'

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mov'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)