import tkinter as tk

window= tk.Tk() #Ventana Principal

mFrame= tk.Frame(window) #Frame Principal
mFrame.pack(fill="both", expand=True, padx= 5, pady= 5) #Insertar mFrame dentro de window
mFrame.config(bg= "lightblue")

for i in range(3):
    for j in range(3):    
        col = tk.Frame(mFrame, borderwidth= 1, width=150, height=150, bg="white", relief="solid")
        col.grid(row= j, column= i, padx= 1, pady= 1)
        if i == 0 and j == 0:
            col.config(bg= "green")
        elif i == 1 and j == 2:
            col.config(bg= "blue")
        elif i == 2 and j == 1:
            col.config(bg= "red")
    
window.mainloop()
