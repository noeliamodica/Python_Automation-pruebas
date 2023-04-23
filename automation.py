import pyautogui 
import time

#time.sleep(6)
#position = pyautogui.position()
#print(position)

pyautogui.moveTo(1038, 1055, duration=1)
pyautogui.click()
time.sleep(3)

pyautogui.moveTo(454, 488, duration=1)
pyautogui.click()
time.sleep(3)


pyautogui.typewrite("youtube")
time.sleep(2)
pyautogui.hotkey('enter')