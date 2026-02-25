import keyboard
import time

TIMER = input("Time before each Autosave:")
time.sleep(TIMER)


keyboard.write(TIMER, delay=0.1)
