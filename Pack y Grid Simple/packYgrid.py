import tkinter as tk
from tkinter import messagebox

def boton():
	messagebox.showinfo("Alerta", "boton tocado")
	
window = tk.Tk() #Ventana principal
window.title("Pack y Grid")

mainFrame = tk.Frame(window, width=200, height=200)#Contenedor Principal
mainFrame.pack()

framePack = tk.Frame(mainFrame, padx=100, pady=100)#Contenedor lado del metodo Pack
framePack.pack(side="left", fill="y")
#Config de "framePack"
framePack.config(width=200, height=200, bg ="blue")

#Widget de prueba, lado Pack
label = tk.Label(framePack, text="Mundo, presente en framePack")
label.pack(padx=10, pady=10)

frameGrid = tk.Frame(mainFrame, padx=100, pady=100)#Contenedor lade del metodo Grid
frameGrid.pack(side="right")
#Config de "frameGrid"
frameGrid.config(width=200, height=200, bg ="green")

##Widget de prueba, lado Grid
button = tk.Button(frameGrid, text="boton si en frameGrid", command=boton)
button.grid(row =1, column =0, padx=10, pady=10)

window.mainloop()
