import customtkinter as CTK
import keyboard
import time


app = CTK.CTk()  
app.geometry("400x240")
app.title("PyAutosave")

def COUNTDOWN():
    TIMER_INT = int(input("Time before each Autosave:"))
    time.sleep(TIMER_INT)
    keyboard.press_and_release('ctrl + s')
    print("Save Successfully!!")

TITLE_HEADER = CTK.CTkLabel(master=app, text="PYTHON AUTOSAVE", font= ("bold",20))
TITLE_HEADER.pack(pady=20)
slider = CTK.CTkSlider(master=app, from_=60, to=600, )
slider.pack(pady=40)

button = CTK.CTkButton(master=app, text="START", command=COUNTDOWN)
button.pack(padx=15, pady=10)

app.mainloop()