import customtkinter
''' for normal tkinter
import tkinter
root = tkinter.Tk()
label = tkinter.Label(root, )
label.pack()
'''
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
root = customtkinter.CTk()
root.geometry("500x350")

def login():
    print("Test")

frame= customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label=customtkinter.CTkLabel(master=root, text="Login System", text_font=("Merriweather"))
label.pack(pady=12, padx=10)

entry1= customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2= customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button=customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox= customtkinter.CTkCheckBox(master=frame, text= "Remember Me")
checkbox.pack(pady=12, padx=10)

root.mainloop()
