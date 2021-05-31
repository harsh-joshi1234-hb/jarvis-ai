import time
from tkinter import *


window = Tk()

window.geometry('500x70')
window.configure(background="black")
window.resizable(0,0)
# window.overrideredirect(1)

def start():
    text= time.strftime("%H:%M:%S  ")
    # text1= time.strftime("%D  ")
    text= time.asctime(time.localtime(time.time()))
    label.config(text=text)
    # label.config(text=text1)
    label.after(200,start)
    

label = Label(window,font=("black",30,"bold"),fg="red",bd=10,bg="black")
label.grid(row= 5,column=5)
start()
print("done")
window.mainloop()

