#The comments are in Spanish
import random #Importamos la libreria "random" para el uso de sus funciones

number = random.randint(1, 100) #Creamos la varible "number" y con "randint" le asignamos un valor aleatorio entre 1 y 100 
numD = int(input("Que numero es: ")) #Le pido al usuario el primer intento de adivinar

while numD != number:   # Mientras numD sea diferente a "number"
    if numD < number:   #Si numD es menor a "number"
        print("muy bajo")#Decir que es muy bajo
    else:                #Sino
        print("Muy alto")#Decir que es muy alto
    numD = int(input("Proba denuevo: "))#Preguntar denuevo

print("Bien ahi")#Terminada la verificacion, nos confirma la respuesta con un texto
#El programa se cierra directamente después de haber impreso el texto
