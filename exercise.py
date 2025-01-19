import os
import time
import requests
from pathlib import Path
from shutil import move

MONITOR_DIR = Path(r"D:\photos")
UPLOADED_DIR = MONITOR_DIR / "uploaded"
UPLOAD_URL = "https://projects.benax.rw/f/o/r/e/a/c/h/p/r/o/j/e/c/t/s/4e8d42b606f70fa9d39741a93ed0356c/iot_testing_202501/upload.php"

UPLOADED_DIR.mkdir(exist_ok=True)

def upload_file(file_path):
    """Uploads a file to the server."""
    try:
        with file_path.open("rb") as file:
            response = requests.post(UPLOAD_URL, files={"imageFile": file})
        if response.status_code == 200:
            print(f"Upload successful: {file_path}")
            return True
        else:
            print(f"Upload failed for {file_path}: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"Error during upload: {e}")
        return False

def process_files():
    """Processes files in the monitored folder."""
    for file_path in MONITOR_DIR.iterdir():
        if file_path.is_file() and time.time() - file_path.stat().st_mtime >= 30:
            if upload_file(file_path):
                move(str(file_path), str(UPLOADED_DIR / file_path.name))

def monitor_folder():
    """Continuously monitors the folder for new files."""
    print(f"Monitoring folder: {MONITOR_DIR}")
    while True:
        process_files()
        time.sleep(10)

if __name__ == "__main__":
    monitor_folder()
