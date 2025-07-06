# Auto Screenshot Taker
A Python script that takes a screenshot of your screen every 10 seconds saving it as screenshot.png, overwriting the previous image each time.

## Features
-Captures a screenshot every 10 seconds
-Saves it as screenshot.png in the current working directory
-Useful for basic screen monitoring or automating simple tasks

## Requirements
```
Python 3.x
pyautogui
```
1. Install the required package:
```
pip install pyautogui
```
2. Run command
```
python screenCapture.py
```
3. This will start an infinite loop that takes a screenshot every 10 seconds and saves it as screenshot.png.

### Example Output

Each screenshot will be saved like this (and overwritten every 10 seconds):
```
screenshot.png
```
To stop the script, press Ctrl + C.

### Warnings
-This script overwrites screenshot.png every cycle. To save unique screenshots, you can modify the script to include timestamps.
-The script runs indefinitely unless manually stopped.
-On macOS or Linux, you might need to give screen recording permissions.
