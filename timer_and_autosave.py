import time
import keyboard

def TIME_INT(timer_int):
    timer_int = int(input("Enter Autosave intervals"))

def countdown(time_sec):
    
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
    
    print("5mins has passed...")
    print("Autosaving...")
    keyboard.press_and_release('ctrl + s')
    print("Save Successfully!!")

TIME_INT()
#fix to make it loop better
count = 0
while count < 5:
    countdown(2)