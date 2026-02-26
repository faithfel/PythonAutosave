import keyboard
import time

def COUNTDOWN():
    TIMER_INT = int(input("Time before each Autosave:"))
    time.sleep(TIMER_INT)
    keyboard.press_and_release('ctrl + s')
    print("Save Successfully!!")

COUNTDOWN()