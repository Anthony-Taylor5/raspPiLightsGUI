import customtkinter
import subprocess
''' for normal tkinter
import tkinter
root = tkinter.Tk()
label = tkinter.Label(root, )
label.pack()

entry1= customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)
checkbox= customtkinter.CTkCheckBox(master=frame, text= "Remember Me")
checkbox.pack(pady=12, padx=10)

'''
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
root = customtkinter.CTk()
root.geometry("500x350")
statusOne=False
statusTwo=False
statusThree=False

def activateOne():
    global statusOne
    if(statusOne==True):
        result = subprocess.run("raspi-gpio set 13 op pn dl", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        statusOne=False    
    else:
        result = subprocess.run("raspi-gpio set 13 op pn dh", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        statusOne=True

def activateTwo():
    global statusTwo
    if(statusTwo==True):
        result = subprocess.run("raspi-gpio set 19 op pn dl", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        statusTwo=False
    else:
        result = subprocess.run("raspi-gpio set 19 op pn dh", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        statusTwo=True

def activateThree():
    global statusThree
    if(statusThree==True):
        result = subprocess.run("raspi-gpio set 26 op pn dl", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        statusThree=False    
    else:
        result = subprocess.run("raspi-gpio set 26 op pn dh", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        statusThree=True

def colorOne():
    global statusOne, statusTwo, statusThree

'''

import subprocess

# Example command: ls (list files in the current directory)
command = "ls"

# Run the command and capture the output
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Print the result
print("Output:", result.stdout)
print("Errors:", result.stderr)
print("Return code:", result.returncode)
'''

label=customtkinter.CTkLabel(master=root, text="Lighting Options", font=("Merriweather", 50))
label.pack(pady=12, padx=10)

frame= customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

button=customtkinter.CTkButton(master=frame, text="Light One", command=activateOne)
button.pack(pady=12, padx=10)

button=customtkinter.CTkButton(master=frame, text="Light Two", command=activateTwo)
button.pack(pady=12, padx=10)

button=customtkinter.CTkButton(master=frame, text="Light Three", command=activateThree)
button.pack(pady=12, padx=10)
'''
checkbox= customtkinter.CTkCheckBox(master=frame, text= "Light Three Option 1", command= )
checkbox.pack(pady=12, padx=10)
checkbox= customtkinter.CTkCheckBox(master=frame, text= "Light Three Option 2", command= )
checkbox.pack(pady=12, padx=10)
checkbox= customtkinter.CTkCheckBox(master=frame, text= "Light Three Option 3", command= )
checkbox.pack(pady=12, padx=10)
'''
root.mainloop()
