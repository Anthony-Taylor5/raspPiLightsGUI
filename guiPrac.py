import customtkinter
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

def activateFour():
    global statusFour
    if(statusFour==True):
        result = subprocess.run("raspi-gpio set 21 op pn dl", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        statusFour=False    
    else:
        result = subprocess.run("raspi-gpio set 21 op pn dh", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        statusFour=True

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
label.grid(pady=12, padx=10, sticky="w")

label=customtkinter.CTkLabel(master=frame, text="Basic Light: ", font=("Merriweather", 30))
label.grid(pady=12, padx=10, sticky="w")

'''
canvas = tk.Canvas(bg='#FAFAFA', selectforeground='#BBDEFB')
    rectangle = canvas.create_rectangle((canvas.winfo_reqwidth() / 2) + 100,
                                         (canvas.winfo_reqheight() / 2) + 50,
                                         (canvas.winfo_reqwidth() / 2) + 150,
                                         (canvas.winfo_reqheight() / 2) + 100,
                                         fill='#FF4081', width=0)
    canvas.grid()
    color = canvas.itemcget(rectangle, "fill")
    print(color)
'''
root.mainloop()
