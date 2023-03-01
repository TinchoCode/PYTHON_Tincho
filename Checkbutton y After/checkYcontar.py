import tkinter as tk
from tkinter import BooleanVar #Libreria necesario

window = tk.Tk()
window.title("Cierto o Mentira")

frame= tk.Frame(window)
frame.pack(ipadx=20, ipady=20)
frame.config(width = 200, height = 200, bg ="green")

def bip():
    if var.get(): #Nos fijamos el estado del boton, si es True: 
        print("Cierto") #Imprime cierto
        window.after(2000, bip)#Y establece que despues de 2 segundos lo vuelva a imprimir
    else: #sino
        print("Mentiras") #Imprime mentiras una vez
        # Como curiosidad si desactivas el boton antes de ke imprima el siguiente cierto imprime un mentiras por el cambio de estado, 
        # y un segundo mentiras ya ke ya estaba en cola el siguiente "bip()"
    

var = BooleanVar(value =False) #Establecemos el tipo Boleano, y lo iniciamos como "False" 
checkButton = tk.Checkbutton(frame, text ="estoy", variable=var, command=bip)# Creacion del Checkbutton
checkButton.pack()

window.mainloop()
