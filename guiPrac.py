import customtkinter
import tkinter
import subprocess

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
root = customtkinter.CTk()
root.geometry("700x500")
statusOne=False
statusTwo=False
statusThree=False
statusFour=False

def activateOne():
    global statusOne, canvasA
    if(statusOne==True):
        result = subprocess.run("raspi-gpio set 13 op pn dl", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        statusOne=False    
        
    else:
        result = subprocess.run("raspi-gpio set 13 op pn dh", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        statusOne=True
        canvasA.configure(bg="red")

def activateTwo():
    global statusTwo, canvasA
    if(statusTwo==True):
        result = subprocess.run("raspi-gpio set 19 op pn dl", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        statusTwo=False
    else:
        result = subprocess.run("raspi-gpio set 19 op pn dh", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        statusTwo=True
        canvasA.configure(bg="green")

def activateThree():
    global statusThree, canvasA
    if(statusThree==True):
        result = subprocess.run("raspi-gpio set 26 op pn dl", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        statusThree=False    
    else:
        result = subprocess.run("raspi-gpio set 26 op pn dh", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        statusThree=True
        canvasA.configure(bg="blue")

def activateFour():
    global statusFour, canvasB
    if(statusFour==True):
        result = subprocess.run("raspi-gpio set 21 op pn dl", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        statusFour=False    
        canvasB.configure(bg="black")
        
    else:
        result = subprocess.run("raspi-gpio set 21 op pn dh", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        statusFour=True
        canvasB.configure(bg="white")

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


checkbox= customtkinter.CTkCheckBox(master=frame, text= "Multi Light: Red", font=("Merriweather", 20), command=activateOne)
checkbox.grid(row=0, column=0, pady= 10, sticky="w")
checkbox= customtkinter.CTkCheckBox(master=frame, text= "Multi Light: Green",  font=("Merriweather", 20), command=activateTwo )
checkbox.grid(row=1, column=0, pady=10, sticky="w")
checkbox= customtkinter.CTkCheckBox(master=frame, text= "Multi Light: Blue",  font=("Merriweather", 20), command=activateThree )
checkbox.grid(row=2, column=0, pady=10, sticky="w")
checkbox= customtkinter.CTkCheckBox(master=frame, text= "Basic Light", font=("Merriweather", 20), command=activateFour)
checkbox.grid(row=3, column=0, pady=10, sticky="w")


label=customtkinter.CTkLabel(master=frame, text="Multi Light: ", font=("Merriweather", 30))
label.grid(row=4, column=0,pady=12, padx=10, sticky="w")

label=customtkinter.CTkLabel(master=frame, text="Basic Light: ", font=("Merriweather", 30))
label.grid(row=5, column=0,pady=12, padx=10, sticky="w")


canvasA = customtkinter.CTkCanvas(master= frame, bg='black', width=300, height=50)
canvasA.grid(row=4, column=3,pady=12, padx=10, sticky="e")

canvasB = customtkinter.CTkCanvas(master= frame, bg='black',width=300, height =50)
canvasB.grid(row=5, column=3,pady=12, padx=10, sticky="e")



root.mainloop()
