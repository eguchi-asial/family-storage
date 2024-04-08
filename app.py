from flask import Flask, render_template, request, redirect
from PIL import Image
import logging
import os
import mimetypes

app = Flask(__name__)
# テンプレートが変更されたとき、再読み込みする
app.config['TEMPLATES_AUTO_RELOAD'] = True

UPLOAD_FOLDER = '/mnt/share'
THUMBNAIL_SIZE = (500, 500)
THUMBNAIL_DIR = "/mnt/share/thumbnail"
IMAGE_DIR = '/mnt/share'

@app.route('/')
def index():
    # Get only the thumbnail images
    thumbnail_files = [
        f for f in os.listdir(THUMBNAIL_DIR)
        if os.path.isfile(os.path.join(THUMBNAIL_DIR, f))
        and not f.startswith('._')
        and (
            f.endswith('.png')
            or f.endswith('.jpg')
            or f.endswith('.jpeg')
            or f.endswith('.gif')
        )
    ]
    return render_template('index.html', image_files=thumbnail_files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        logging.warning('No file part')
        return redirect('/')
    files = request.files.getlist('file')
    for file in files:
        if file.filename == '':
            logging.warning('No selected file')
            return redirect('/')
        if not allowed_file(file.filename):
            logging.warning('File type not allowed')
            continue  # Skip this file and move to the next one
        mimetype = mimetypes.guess_type(file.filename)[0]
        # TODO 今はまだ画像のみ対応
        if not mimetype or not mimetype.startswith('image'):
            logging.warning('File is not an image')
            continue  # Skip this file and move to the next one
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        # Open the image file
        with Image.open(os.path.join(IMAGE_DIR, file.filename)) as img:
            # Create a thumbnail
            img.thumbnail(THUMBNAIL_SIZE)
            # Save the thumbnail to a new file in the specified directory
            img.save(os.path.join(THUMBNAIL_DIR, 'thumbnail_' + file.filename))
    return redirect('/')

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mov'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/delete', methods=['POST'])
def delete_files():
    files_to_delete = request.get_json()
    for filename in files_to_delete:
        # filenameに「thumbnail_」が付いているので、元のファイル名に戻す
        os.remove(os.path.join(UPLOAD_FOLDER, filename.replace("thumbnail_", "")))
        os.remove(os.path.join(THUMBNAIL_DIR, filename))
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)