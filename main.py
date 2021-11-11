from pynput.mouse import Button, Controller
import keyboard as kb
import time

mouse = Controller()

ACTIVATE = "ctrl"
TERMINATE = "esc"
INTERVAL = 0.01

print(f"Starting in 5 seconds. Hold down {ACTIVATE} key to autoclick.")
time.sleep(5)

print(f"Script active. Press the {TERMINATE} key to end.")
while True:
    if kb.is_pressed(ACTIVATE):
        mouse.press(Button.left)
        mouse.release(Button.left)
    elif kb.is_pressed(TERMINATE):
        break
    time.sleep(INTERVAL)
