import os
import imagehash
from PIL import Image

def calculate_hash(filepath):
    with Image.open(filepath) as img:
        return imagehash.average_hash(img)

def find_duplicates(directory_path):
    file_dict = {}
    # os.walkだとサブディレクトリまで再帰的に探索するが、os.scandirは指定ディレクトリのみ
    for entry in os.scandir(directory_path):
        if entry.is_file():
            file_path = entry.path
            file_hash = calculate_hash(file_path)
            # UNIX時間の取得
            modified_time = os.path.getmtime(file_path)
            if file_hash in file_dict:
                # If the current file is older, delete it
                if modified_time < file_dict[file_hash][1]:
                    os.remove(file_path)
                # If the current file is newer, delete the older one
                else:
                    os.remove(file_dict[file_hash][0])
                    file_dict[file_hash] = (file_path, modified_time)
            else:
                file_dict[file_hash] = (file_path, modified_time)

find_duplicates('/mnt/share')
find_duplicates('/mnt/share/thumbnail')
