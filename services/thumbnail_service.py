# services/thumbnail_service.py
import os
from config import THUMBNAIL_DIR

def get_thumbnail_files():
    return [
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