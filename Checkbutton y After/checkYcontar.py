import tkinter as tk
from tkinter import BooleanVar
import time

window = tk.Tk()
window.title("Cierto o Mentira")

frame= tk.Frame(window)
frame.pack(ipadx=20, ipady=20)
frame.config(width = 200, height = 200, bg ="green")

def bip():
    if var.get():
        print("Cierto")
        window.after(2000, bip)
    else:
        print("Mentiras")
    

var = BooleanVar(value =False)
checkButton = tk.Checkbutton(frame, text ="estoy", variable=var, command=bip)
checkButton.pack()

window.mainloop()
