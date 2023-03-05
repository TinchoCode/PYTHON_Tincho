import tkinter as tk

window= tk.Tk()
window.title("Menus")

mFrame= tk.Frame(window) #Main Frame
mFrame.pack(fill= "both", expand= True, padx= 5, pady= 5)
mFrame.config(bg= "black")

menuF= tk.Frame(mFrame, bg= "red") #Frame para menu
menuF.pack(fill= "x")

for i in range(5):
#Cuadros del menu
    col= tk.Frame(menuF, borderwidth= 1, relief= "solid", width= 50, height= 20, bg= "yellow")
    col.grid(row=0, column= i, padx= 1, pady= 1)
#InstaBotones del menu
    si= str(i + 1)
    button= tk.Button(menuF, borderwidth= 1, relief= "solid", bg= "yellow", text= "Soy "+si)
    button.grid(row=1, column= i, padx= 1, pady= 1)

cuadroF= tk.Frame(mFrame, bg= "lightblue", height= 100)
cuadroF.pack(fill="both", expand= True)
cuadroF.propagate(False)

veo= tk.Label(cuadroF, text="Soy el mundo")
veo.pack()

window.mainloop()
