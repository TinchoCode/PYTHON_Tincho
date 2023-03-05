import tkinter as tk

window= tk.Tk()
window.title("Menus")

mFrame= tk.Frame(window) #Main Frame
mFrame.pack(fill= "both", expand= True, padx= 5, pady= 5)
mFrame.config(bg= "black")

menuF= tk.Frame(mFrame, bg= "red") #Frame para el menu
menuF.pack(fill= "x")

for i in range(5): #Loop para crear cada item
#Fila de Frames
    col= tk.Frame(menuF, borderwidth= 1, relief= "solid", width= 50, height= 20, bg= "blue")
    col.grid(row=0, column= i, padx= 1, pady= 1)
#Fila de Botones (Sin uso)
    si= str(i + 1) #Agrego esta variable string para poder concatenarla en el text
    button= tk.Button(menuF, borderwidth= 1, relief= "solid", bg= "yellow", text= "Soy "+si)
    button.grid(row=1, column= i, padx= 1, pady= 1)

cuadroF= tk.Frame(mFrame, bg= "lightblue", height= 100) #Aca establezco el height
cuadroF.pack(fill="both", expand= True)
cuadroF.propagate(False) #Con esto evito que tome las medidas del "Padre" y use la establecida por mi

veo= tk.Label(cuadroF, text="Soy el mundo") #Label agregado para que el segundo Frame no este vacio
veo.pack()

window.mainloop()
