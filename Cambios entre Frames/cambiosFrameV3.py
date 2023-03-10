import tkinter as tk

class Interface:
    def __init__(self, window):
        self.window= window
        self.window.title("Cambios entre Frames con Ayuda")

        self.posActual=1 #Variable Global de posicion

        self.mFrame= tk.Frame(window) #Main Frame
        self.mFrame.pack(fill= "both", expand= True, padx= 5, pady= 5)
        self.mFrame.config(bg= "black")

        self.menuF= tk.Frame(self.mFrame, bg= "red") #Frame para menu
        self.menuF.pack(fill= "x")
        
        self.frames= []  #Array para futuros Frames
        self.create_frames() #Funcion de creacion de los Frames
        self.create_butons() #Funcion de creacion de los Botones

    def create_frames(self):
        #Frames
        colores= ["lightblue", "orange", "purple", "red", "green"]
        for i in range(5):
            frame= tk.Frame(self.mFrame, bg= colores[i], height= 150)
            frame.propagate(False)
            leo= tk.Label(frame, text=f"Soy el mundo en F{i+1}") #Label para el texto
            leo.pack()
            self.frames.append(frame) #Lo Agrego al array
        self.frames[0].pack(fill="both", expand= True) #Muestro unicamente el Primer Frame
        
    def create_butons(self):
        for i in range(len(self.frames)):
                button = tk.Button(self.menuF, borderwidth= 1, relief= "solid", bg= "yellow", text=f"Frame {i+1}", command=lambda i=i: self.cambio(i + 1))
                button.grid(row=1, column= i, padx= 1, pady= 1)

    def cambio(self, voy):
        if self.posActual != voy:
            self.frames[self.posActual - 1].pack_forget()
            self.frames[voy - 1].pack(fill="both", expand=True)
            self.posActual = voy 
        return self.posActual

window = tk.Tk()
app = Interface(window)
window.mainloop()
