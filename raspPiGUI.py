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

def configureMultiLight(redStatus, greenStatus, blueStatus):
    if(redStatus and greenStatus and blueStatus):
            canvasA.configure(bg="teal")
    elif(redStatus and blueStatus):
        canvasA.configure(bg="purple")
    elif(redStatus and greenStatus):
        canvasA.configure(bg="#9ACD32")
    elif(greenStatus and blueStatus):
        canvasA.configure(bg="dark blue")
    elif(redStatus):
        canvasA.configure(bg="red")
    elif(greenStatus):
        canvasA.configure(bg="green")
    elif(blueStatus):
        canvasA.configure(bg="blue")
    else:
        canvasA.configure(bg="black")



def activateOne():
    global statusOne,statusTwo, statusThree, canvasA
    if(statusOne==True):
        result = subprocess.run("raspi-gpio set 13 op pn dl", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        statusOne=False        
        configureMultiLight(statusOne, statusTwo, statusThree)

    else:
        result = subprocess.run("raspi-gpio set 13 op pn dh", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        statusOne=True
        configureMultiLight(statusOne, statusTwo, statusThree)

def activateTwo():
    global statusOne,statusTwo, statusThree, canvasA
    if(statusTwo==True):
        result = subprocess.run("raspi-gpio set 19 op pn dl", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        statusTwo=False
        configureMultiLight(statusOne, statusTwo, statusThree)

    else:
        result = subprocess.run("raspi-gpio set 19 op pn dh", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        statusTwo=True
        configureMultiLight(statusOne, statusTwo, statusThree)

 
def activateThree():
    global statusOne,statusTwo, statusThree, canvasA
    if(statusThree==True):
        result = subprocess.run("raspi-gpio set 26 op pn dl", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        statusThree=False
        configureMultiLight(statusOne, statusTwo, statusThree)

       
    else:
        result = subprocess.run("raspi-gpio set 26 op pn dh", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        statusThree=True
        configureMultiLight(statusOne, statusTwo, statusThree)

        

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
checkbox.grid(row=0, column=0, pady= 10,padx=10, sticky="w")
checkbox= customtkinter.CTkCheckBox(master=frame, text= "Multi Light: Green",  font=("Merriweather", 20), command=activateTwo )
checkbox.grid(row=1, column=0, pady=10, padx=10, sticky="w")
checkbox= customtkinter.CTkCheckBox(master=frame, text= "Multi Light: Blue",  font=("Merriweather", 20), command=activateThree )
checkbox.grid(row=2, column=0, pady=10, padx=10, sticky="w")
checkbox= customtkinter.CTkCheckBox(master=frame, text= "Basic Light", font=("Merriweather", 20), command=activateFour)
checkbox.grid(row=3, column=0, pady=10, padx=10, sticky="w")


label=customtkinter.CTkLabel(master=frame, text="Multi Light: ", font=("Merriweather", 30))
label.grid(row=4, column=0,pady=12, padx=10, sticky="w")

label=customtkinter.CTkLabel(master=frame, text="Basic Light: ", font=("Merriweather", 30))
label.grid(row=5, column=0,pady=12, padx=10, sticky="w")


canvasA = customtkinter.CTkCanvas(master= frame, bg='black', width=300, height=50)
canvasA.grid(row=4, column=3,pady=12, padx=10, sticky="e")

canvasB = customtkinter.CTkCanvas(master= frame, bg='black',width=300, height =50)
canvasB.grid(row=5, column=3,pady=12, padx=10, sticky="e")



root.mainloop()
