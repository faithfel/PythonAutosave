import customtkinter as CTK
import keyboard
import time



app = CTK.CTk()  
app.geometry("400x240")
app.title("PyAutosave")

TITLE_HEADER = CTK.CTkLabel(master=app, text="PYTHON AUTOSAVE", font= ("bold",20))
TITLE_HEADER.pack(pady=20)


def START_TIMER():
    TIMER_VAL = entry.get()
    print(TIMER_VAL)
    time.sleep(int(TIMER_VAL))
    keyboard.press_and_release('ctrl + s')
    print("Save Successfully!!")


entry = CTK.CTkEntry(app, placeholder_text="CTkEntry")
entry.pack(pady=20, padx=20)
entry.get


button = CTK.CTkButton(master=app, text="START", command=START_TIMER)
button.pack(padx=15, pady=10)

app.mainloop()