import pyautogui
import time
import os
from datetime import datetime

while True:
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    time.sleep(10)