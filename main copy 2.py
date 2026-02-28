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


ENTRY = CTK.CTkEntry(app, placeholder_text="Type Time Interval Here")
ENTRY.pack(pady=5, padx=20)
ENTRY.get

toggle_var = tkinter.IntVar(value=0)

def get_toggle_state():

    TOGGLE_STATE = toggle_var.get()
    print(f"Current state: {TOGGLE_STATE}")
    TIMER_VAL = ENTRY.get()
    
    
    while TOGGLE_STATE == 1:  
        time.sleep(int(TIMER_VAL))
        mins, secs = divmod(int(TIMER_VAL), 60)
        TIMER_FORMAT = '{:02d}:{:02d}'.format(mins, secs)
        print(f" Autosave is set at {TIMER_FORMAT}!")
        time.sleep(1)  
           
    keyboard.press_and_release('ctrl + s')
    print("Save Successfully!!")


   

toggle_button = tkinter.Checkbutton(
    app,
    text="Toggle Button",
    variable=toggle_var,
    indicatoron=False, 
    width=15,
    command=get_toggle_state
)


    
toggle_button.pack(pady=20)

class StdoutRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.insert(tkinter.END, string)
        self.text_widget.see(tkinter.END) 

    def flush(self):
        pass



text = tkinter.Text(app)
text.pack()
sys.stdout = StdoutRedirector(text)



app.mainloop()