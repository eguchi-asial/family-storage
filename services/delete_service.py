# services/delete_service.py
import os
from config import UPLOAD_FOLDER, THUMBNAIL_DIR

def delete_files(files_to_delete):
    for filename in files_to_delete:
        os.remove(os.path.join(UPLOAD_FOLDER, filename))
        # filenameに「thumbnail_」が必要で末尾が「.png」で終わる
        base_name = os.path.splitext(filename)[0]
        extension = os.path.splitext(filename)[1]
        if extension in ['.mp4', '.avi', '.mov']:  # Add more video formats if needed
            os.remove(os.path.join(THUMBNAIL_DIR, f'thumbnail_{base_name}_movie.png'))
        else:
            os.remove(os.path.join(THUMBNAIL_DIR, f'thumbnail_{base_name}.png'))
