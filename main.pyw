import webbrowser as wb
import time
import pynput
from pynput.keyboard import Key, Controller

time.sleep(15)
wb.open("https://shattereddisk.github.io/rickroll/rickroll.mp4")

time.sleep(2)

keyboard = Controller()

keyboard.press('F11')