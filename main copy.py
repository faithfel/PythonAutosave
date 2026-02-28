import customtkinter as CTK
import keyboard
import time
import tkinter 
import tkinter.scrolledtext as TKST
import sys

app = CTK.CTk()  
app.geometry("400x240")
app.title("PyAutosave")
CTK.set_appearance_mode("Dark")
CTK.set_default_color_theme("themes/orange.json")

TITLE_HEADER = CTK.CTkLabel(master=app, text="PYTHON AUTOSAVE", font=("Impact", 40))
TITLE_HEADER.pack(pady=15)

def countdown(time_sec):
    
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
    

def START_TIMER():
    
    TIMER_VAL = ENTRY.get()
    mins, secs = divmod(int(TIMER_VAL), 60)
    TIMER_FORMAT = '{:02d}:{:02d}'.format(mins, secs)
    print(f" Autosave is set at {TIMER_FORMAT}!", end='\r')
    time.sleep(1)
    time.sleep(int(TIMER_VAL))



    keyboard.press_and_release('ctrl + s')
    print("Save Successfully!!")



ENTRY = CTK.CTkEntry(app, placeholder_text="CTkEntry")
ENTRY.pack(pady=5, padx=20)
ENTRY.get


BUTTON = CTK.CTkButton(master=app, text="START", command=START_TIMER)
BUTTON.pack(padx=5, pady=10)




edit_area = TKST.ScrolledText(
    app,
    wrap=tkinter.WORD,  
    width=40,
    height=15,
    bg="black",   
    fg="white",      
    font=("courier", 12)
)

edit_area.pack(padx=10, pady=10, fill=tkinter.BOTH, expand=True)


#def REDIRECT(object):
   


#sys.stdout.write = REDIRECT(edit_area)

PLACEHOLDER = "Terminal Output" * 1
edit_area.insert(tkinter.INSERT, PLACEHOLDER)

app.mainloop()