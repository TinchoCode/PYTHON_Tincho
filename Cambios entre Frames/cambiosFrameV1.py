import tkinter as tk

window= tk.Tk()
window.title("Cambios entre Frames")

posActual=1 #Variable Global de posicion, empezando en el Frame 1
        
mFrame= tk.Frame(window) #Main Frame
mFrame.pack(fill= "both", expand= True, padx= 5, pady= 5)
mFrame.config(bg= "black")

menuF= tk.Frame(mFrame, bg= "red") #Frame para menu
menuF.pack(fill= "x")

#Frames
#Frame 1
cuadroF1= tk.Frame(mFrame, bg= "lightblue", height= 100)
cuadroF1.pack(fill="both", expand= True)
cuadroF1.propagate(False)

veo= tk.Label(cuadroF1, text="Soy el mundo en F1")
veo.pack()
#Frame 2
cuadroF2= tk.Frame(mFrame, bg= "lightblue", height= 100)
#cuadroF2.pack(fill="both", expand= True)
cuadroF2.propagate(False)

veo2= tk.Label(cuadroF2, text="Soy el mundo en F2")
veo2.pack()
cuadroF2.pack_forget() #Escondo el Frame2

#Funcion de cambio
def cambio(voy): 
    global posActual #Uso de la variable GLobal
    if voy == 2 and posActual ==1: #Si voy es 2 y la posicion actual es 1
        cuadroF1.pack_forget() #Escondo el 1
        cuadroF2.pack(fill="both", expand=True) #Muestro el 2
        posActual=2 #Y actualizo la posicion actual
    if voy == 1 and posActual ==2: #Lo mismo pero con el otro frame
        cuadroF2.pack_forget()
        cuadroF1.pack(fill="both", expand=True)
        posActual=1
    return posActual #Retorno el valor de la posicion actual

#Botones
#Boton Frame 1
butFrame1 = tk.Button(menuF, borderwidth= 1, relief= "solid", bg= "yellow", text="Frame1", command=lambda:cambio(1))
butFrame1.grid(row=1, column= 0, padx= 1, pady= 1)
#Boton Frame 2
butFrame2 = tk.Button(menuF, borderwidth= 1, relief= "solid", bg= "yellow", text="Frame2", command=lambda:cambio(2))
butFrame2.grid(row=1, column= 1, padx= 1, pady= 1)

window.mainloop()
