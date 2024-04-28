import sys
from PIL import Image
import imagehash

def calculate_hash(filepath):
    with Image.open(filepath) as img:
        return imagehash.average_hash(img)

def compare_images(image_path1, image_path2):
    hash1 = calculate_hash(image_path1)
    hash2 = calculate_hash(image_path2)

    if hash1 == hash2:
        print(f"The images at {image_path1} and {image_path2} are the same.")
    else:
        print(f"The images at {image_path1} and {image_path2} are not the same.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python checkSame.py <image_path1> <image_path2>")
        sys.exit(1)

    image_path1 = sys.argv[1]
    image_path2 = sys.argv[2]

    compare_images(image_path1, image_path2)
