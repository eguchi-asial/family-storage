# services/upload_service.py
import os
import mimetypes
from PIL import Image
from config import UPLOAD_FOLDER, THUMBNAIL_SIZE, THUMBNAIL_DIR, IMAGE_DIR, ALLOWED_EXTENSIONS

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

import subprocess

def upload_files(files):
    for file in files:
        if file.filename == '':
            return False, 'No selected file'
        if not allowed_file(file.filename):
            return False, 'File type not allowed'
        mimetype = mimetypes.guess_type(file.filename)[0]
        if not mimetype:
            return False, 'File type could not be determined'
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        if mimetype.startswith('image'):
            with Image.open(os.path.join(IMAGE_DIR, file.filename)) as img:
                img.thumbnail(THUMBNAIL_SIZE)
                img.save(os.path.join(THUMBNAIL_DIR, 'thumbnail_' + file.filename))
        elif mimetype.startswith('video'):
            thumbnail_filename = 'thumbnail_' + file.filename.rsplit('.', 1)[0] + '_movie.jpg'
            subprocess.run(['ffmpeg', '-i', os.path.join(UPLOAD_FOLDER, file.filename), '-ss', '00:00:01.000', '-vframes', '1', '-vf', 'scale=400:400', os.path.join(THUMBNAIL_DIR, thumbnail_filename)])
    return True, None
