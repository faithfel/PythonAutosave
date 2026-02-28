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
    

def START_TIMER(TOGGLE_STATE):

    TIMER_VAL = ENTRY.get()
    mins, secs = divmod(int(TIMER_VAL), 60)
    TIMER_FORMAT = '{:02d}:{:02d}'.format(mins, secs)
    print(f" Autosave is set at {TIMER_FORMAT}!")
    time.sleep(1)
    time.sleep(int(TIMER_VAL))



    keyboard.press_and_release('ctrl + s')
    print("Save Successfully!!")



ENTRY = CTK.CTkEntry(app, placeholder_text="CTkEntry")
ENTRY.pack(pady=5, padx=20)
ENTRY.get

toggle_var = tkinter.IntVar(value=0)

def get_toggle_state():
    # Retrieve the current value of the toggle_var (1 for ON, 0 for OFF)
    TOGGLE_STATE = toggle_var.get()
    print(f"Current state: {TOGGLE_STATE}")

toggle_button = tkinter.Checkbutton(
    app,
    text="Toggle Button",
    variable=toggle_var,
    indicatoron=False, # Hides the default checkbox indicator
    width=15,
    command=get_toggle_state
)


    
toggle_button.pack(pady=20)






app.mainloop()