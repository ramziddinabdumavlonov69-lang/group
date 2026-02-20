
import os
import shutil

FILES_DIR = "files"

if not os.path.exists(FILES_DIR):
    os.makedirs(FILES_DIR)

def save_file(filepath):
    filename = os.path.basename(filepath)
    destination = os.path.join(FILES_DIR, filename)
    shutil.copy(filepath, destination)
    return filename
