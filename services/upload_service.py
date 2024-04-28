# services/upload_service.py
import os
import mimetypes
from PIL import Image
from config import UPLOAD_FOLDER, THUMBNAIL_SIZE, THUMBNAIL_DIR, IMAGE_DIR

def allowed_file(filename):
    # 動画はまだ対応していないのでコメントアウト
    # ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mov'}
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_files(files):
    for file in files:
        if file.filename == '':
            return False, 'No selected file'
        if not allowed_file(file.filename):
            return False, 'File type not allowed'
        mimetype = mimetypes.guess_type(file.filename)[0]
        if not mimetype or not mimetype.startswith('image'):
            return False, 'File is not an image'
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        with Image.open(os.path.join(IMAGE_DIR, file.filename)) as img:
            img.thumbnail(THUMBNAIL_SIZE)
            img.save(os.path.join(THUMBNAIL_DIR, 'thumbnail_' + file.filename))
    return True, None
