import keyboard
import time

TIMER = int(input("Time before each Autosave:"))
time.sleep(TIMER)

keyboard.press_and_release('ctrl + s')
print("Save Successfully!!")
