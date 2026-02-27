import customtkinter as CTK
import keyboard
import time


app = CTK.CTk()  
app.geometry("400x240")
app.title("PyAutosave")



def SLIDER_CALLBACK(value):
    print(value)
    time.sleep(value)
    keyboard.press_and_release('ctrl + s')
    print("Save Successfully!!")

TITLE_HEADER = CTK.CTkLabel(master=app, text="PYTHON AUTOSAVE", font= ("bold",20))
TITLE_HEADER.pack(pady=20)

slider = CTK.CTkSlider(master=app, from_=60, to=600, command=SLIDER_CALLBACK)
slider.pack(pady=40)
slider.set(0)




button = CTK.CTkButton(master=app, text="START", )
button.pack(padx=15, pady=10)

app.mainloop()