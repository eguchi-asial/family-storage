# services/originalfile_service.py
import os

def get_original_files():
    directory = '/mnt/share'
    return [
        f for f in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, f))
        and not f.startswith('._')
        and (
            f.endswith('.png')
            or f.endswith('.jpg')
            or f.endswith('.jpeg')
            or f.endswith('.gif')
            or f.endswith('.mp4')
            or f.endswith('.mov')
            or f.endswith('.avi')
            or f.endswith('.mkv')
            or f.endswith('.flv')
            or f.endswith('.wmv')
            or f.endswith('.webm')
            or f.endswith('.m4v')
            or f.endswith('.3gp')
            or f.endswith('.3g2')
            or f.endswith('.ogv')
            or f.endswith('.mpeg')
            or f.endswith('.mpg')
            or f.endswith('.rm')
            or f.endswith('.swf')
            or f.endswith('.vob')
        )
    ]