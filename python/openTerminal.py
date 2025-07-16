import subprocess
import pyautogui as pa
import time

subprocess.Popen(["alacritty"])
time.sleep(0.5)
pa.write("fastfetch")
pa.press('Enter')
