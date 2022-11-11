import tkinter
from tkinter import messagebox
import subprocess
import os 


# Handle errors while calling os.ulink()
window = tkinter.Tk()
window.title("Genshin Impact Rich Presence")
window.geometry("400x400")
window.iconbitmap(default='images\\ApplicatonIcon.ico')
window.resizable(0, 0)
window.config(bg="white") 



def Start():
    subprocess.Popen('GrabParty.exe'),
    subprocess.Popen('GrabArea.exe')
    subprocess.Popen('RichPresence.bat')

    
def Stop():
    subprocess.call(["taskkill","/F","/IM","GrabArea.exe"])
    subprocess.call(["taskkill","/F","/IM","GrabParty.exe"])    
    os.remove("player.log")
    
myimage = tkinter.PhotoImage(file="images\\StarSnatchCliff.png")

image = tkinter.Label(window, image=myimage, width=500, height=170, )
image.pack()

button = tkinter.Button(text="Start Discord Rich Presence", command=Start)
button.pack(pady=10)

button = tkinter.Button(text="Stop Grabbing Genshin Impact Names (the 2 windows that opened)", command=Stop)
button.pack(pady=10)

button = tkinter.Button(text="to stop the Discord Rich Presence just close this application",
                       bg="black",
                       fg="white")      
button.pack(pady=10)


window.mainloop()   