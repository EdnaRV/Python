import mouse
import time
import pyautogui, sys
while(True):
   mouse.move(50,350,absolute=True,duration=0)
   time.sleep(4)
   pyautogui.click(button='right')
   mouse.move(70,450,absolute=True,duration=0)
   time.sleep(4)
   pyautogui.click(button='right')