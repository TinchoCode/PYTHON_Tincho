import tkinter as tk

window= tk.Tk() #Ventana Principal

mFrame= tk.Frame(window) #Frame Principal
mFrame.pack(fill="both", expand=True, padx= 5, pady= 5) #Parametros: Fill para que el Frame crezca lo necesario, Expand permite crecer si lo necesito.
mFrame.config(bg= "lightblue") #Color de Fondo

for i in range(3): #Loop Creacion de Columnas
    for j in range(3): #Loop Creacion de Filas   
        col = tk.Frame(mFrame, borderwidth= 1, width=150, height=150, bg="white", relief="solid") #Parametros: Relief nos dibuja el border sin ningun estilo particular
        col.grid(row= j, column= i, padx= 1, pady= 1) #Creacion de un 9x9 debido a los loops
        if i == 0 and j == 0: #En la Columna 1 y Fila 1
            col.config(bg= "green") #Fondo Verde
        elif i == 1 and j == 2: #En la Columna 2 y Fila 3
            col.config(bg= "blue") #Fondo Azul
        elif i == 2 and j == 1: #En la Columna 3 y Fila 2
            col.config(bg= "red") #Fondo Rojo
    
window.mainloop()
