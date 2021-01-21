# import (pip install pyautogui)

import pyautogui
import time
while True:
    time.sleep(3)
    pyautogui.typewrite('Hi (Sent by Python Auto Message)')
    pyautogui.press('enter')