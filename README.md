# python
# File Upload Monitor

This project monitors a specific folder for newly added files and automatically uploads them to a remote server. Once uploaded, the files are moved to a separate "uploaded" directory to keep track of which files have been processed.

## Features

- **Monitors a directory**: Continuously monitors a folder for new files.
- **Uploads files**: Automatically uploads files to a specified URL when they are added to the folder.
- **File organization**: Once a file is successfully uploaded, it is moved to a separate "uploaded" directory to prevent re-uploading.

## Prerequisites

- Python 3.6 or higher
- The `requests` library for making HTTP requests

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/python.git
    ```

2. Install the required dependencies:
    ```bash
    pip install requests
    ```

3. Update the following variables in the script:
   - `MONITOR_DIR`: Path to the folder you want to monitor (default is `D:/photos`).
   - `UPLOAD_URL`: The URL endpoint for the file upload.

## How It Works

1. The script monitors the `MONITOR_DIR` folder for new files.
2. Once a file has been in the directory for at least 30 seconds, the script attempts to upload it to the specified `UPLOAD_URL`.
3. If the upload is successful (status code 200), the file is moved to the `uploaded` directory inside `MONITOR_DIR`.
4. The script continues to monitor the folder in a loop, checking every 10 seconds.

## Usage

1. Make sure the script is configured with the correct monitor directory and upload URL.
2. Run the script:
    ```bash
    python file_upload_monitor.py
    ```
3. The script will continue running in the background, uploading new files as they appear.

## Notes

- This script checks for new files every 10 seconds and processes files that have been in the monitored folder for at least 30 seconds.
- Files are uploaded via HTTP POST with the key `"imageFile"`. Ensure the server-side endpoint is properly configured to handle the upload.
- The uploaded files are moved to the `uploaded` folder to avoid re-uploading them.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

