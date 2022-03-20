
import pyautogui as bomb
import time
print("start")
time.sleep(10)

for i in range(10):
    bomb.write("hi")
    time.sleep(0.5)
    bomb.press("enter")