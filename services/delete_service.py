# services/delete_service.py
import os
from config import UPLOAD_FOLDER, THUMBNAIL_DIR

def delete_files(files_to_delete):
    for filename in files_to_delete:
        # filenameに「thumbnail_」が付いているので、元のファイル名に戻す
        os.remove(os.path.join(UPLOAD_FOLDER, filename.replace("thumbnail_", "")))
        os.remove(os.path.join(THUMBNAIL_DIR, filename))