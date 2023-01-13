import random
import subprocess
import time

import pyautogui
import win32gui

counter = 0
waitTime = 5
notepad = subprocess.Popen(['notepad.exe'])
time.sleep((2))
handle = win32gui.FindWindow(None, "Untitled - Notepad")


def runTime(sec):
    seconds = sec
    minutes = seconds // 60
    hours = minutes // 60
    return (f"{hours} H, {minutes%60} M, {seconds%60} S")


while handle:
    try:
        rect = win32gui.GetWindowRect(handle)
        x, y, xWorkableArea, yWorkableArea = rect
        x, y = (random.randint(x, xWorkableArea),
                random.randint(y, yWorkableArea))
        pyautogui.typewrite(f"Load Test :: {runTime(counter)} :: {x},{y}\n")
        pyautogui.moveTo(x, y, duration=0.25)
        print(f"Moved to :: {x},{y}")
        time.sleep(waitTime)
        counter += waitTime

    except:
        print("Notepad not found")
        handle = False
