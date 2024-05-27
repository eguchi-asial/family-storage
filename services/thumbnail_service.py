# services/thumbnail_service.py
import os
from config import THUMBNAIL_DIR

def get_thumbnail_files(original_files):
    thumbnail_files = []
    for original in original_files:
        base_name = os.path.splitext(original)[0]
        extension = os.path.splitext(original)[1]
        if extension in ['.mp4', '.avi', '.mov']:  # Add more video formats if needed
            thumbnail = f'thumbnail_{base_name}_movie.png'
        else:
            thumbnail = f'thumbnail_{base_name}.png'
        if os.path.isfile(os.path.join(THUMBNAIL_DIR, thumbnail)):
            thumbnail_files.append(thumbnail)
    return thumbnail_files