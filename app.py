from flask import Flask, render_template, request, redirect

import os

app = Flask(__name__)
# テンプレートが変更されたとき、再読み込みする
app.config['TEMPLATES_AUTO_RELOAD'] = True

UPLOAD_FOLDER = '/mnt/share'

@app.route('/')
def index():
    image_dir = '/mnt/share'
    image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f)) and not f.startswith('._') and (f.endswith('.png') or f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.gif'))]
    return render_template('index.html', image_files=image_files)

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
    return redirect('/')

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mov'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)