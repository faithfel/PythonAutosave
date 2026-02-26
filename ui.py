import customtkinter as CTK

app = CTK.CTk()  
app.geometry("400x240")
app.title("Installation Test")

def button_event():
    print("button pressed")

button = CTK.CTkButton(app, text="CTkButton", command=button_event)



app.mainloop()