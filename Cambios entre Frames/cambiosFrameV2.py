import tkinter as tk

window= tk.Tk()
window.title("Cambios entre Frames")

posActual=1 #Variable Global de posicion
        
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
veo= tk.Label(cuadroF1, text="Soy el mundo en F1") #Label para el texto
veo.pack()
#Frame 2
cuadroF2= tk.Frame(mFrame, bg= "orange", height= 100)
#cuadroF2.pack(fill="both", expand= True)
cuadroF2.propagate(False)
veo2= tk.Label(cuadroF2, text="Soy el mundo en F2") #Label para el texto
veo2.pack()
cuadroF2.pack_forget() #Escondo el Frame2
#Frame 3
cuadroF3= tk.Frame(mFrame, bg= "purple", height= 100)
#cuadroF2.pack(fill="both", expand= True)
cuadroF3.propagate(False)
veo3= tk.Label(cuadroF3, text="Soy el mundo en F3") #Label para el texto
veo3.pack()
cuadroF3.pack_forget() #Escondo el Frame2

def cambio(voy):
    global posActual
    frame = [cuadroF1, cuadroF2, cuadroF3]
    print("Fuera: ", posActual, voy)
    if posActual != voy:
        posActual-=1
        voy -=1
        print("Adentro: ", posActual, voy)
        frame[posActual].pack_forget()
        frame[voy].pack(fill="both", expand=True)
        posActual = voy + 1
        print("posActual es: ", posActual)
    return posActual

#Botones
#Boton Frame 1
butFrame1 = tk.Button(menuF, borderwidth= 1, relief= "solid", bg= "yellow", text="Frame1", command=lambda:cambio(1))
butFrame1.grid(row=1, column= 0, padx= 1, pady= 1)
#Boton Frame 2
butFrame2 = tk.Button(menuF, borderwidth= 1, relief= "solid", bg= "yellow", text="Frame2", command=lambda:cambio(2))
butFrame2.grid(row=1, column= 1, padx= 1, pady= 1)
#Boton Frame 3
butFrame3 = tk.Button(menuF, borderwidth= 1, relief= "solid", bg= "yellow", text="Frame2", command=lambda:cambio(3))
butFrame3.grid(row=1, column= 2, padx= 1, pady= 1)

window.mainloop()
