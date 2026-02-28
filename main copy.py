import customtkinter as CTK
import keyboard
import time



app = CTK.CTk()  
app.geometry("400x240")
app.title("PyAutosave")
CTK.set_appearance_mode("Dark")
CTK.set_default_color_theme("themes/orange.json")

TITLE_HEADER = CTK.CTkLabel(master=app, text="PYTHON AUTOSAVE", font=("Impact", 40))
TITLE_HEADER.pack(pady=15)


def START_TIMER():
    
    TIMER_VAL = ENTRY.get()
    print(f" Autosave is set at {TIMER_VAL} per seconds!")
    time.sleep(int(TIMER_VAL))
    while COUNTDOWN:
    mins, secs = divmod(time_sec, 60)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    print(timeformat, end='\r')
    time.sleep(1)
    time_sec -= 1
    
    keyboard.press_and_release('ctrl + s')
    print("Save Successfully!!")


ENTRY = CTK.CTkEntry(app, placeholder_text="CTkEntry")
ENTRY.pack(pady=5, padx=20)
ENTRY.get


BUTTON = CTK.CTkButton(master=app, text="START", command=START_TIMER)
BUTTON.pack(padx=5, pady=10)

app.mainloop()