import random

number = random.randint(1, 100)
numD = int(input("Ke numero es: "))

while numD != number:   # Mientras numD sea diferente a number
    if numD < number:   #Si numD es menor a number
        print("muy bajo")#Decir que es muy bajo
    else:                #Sino
        print("Muy alto")#Decir que es muy alto
    numD = int(input("Proba denuevo: "))#Preguntar denuevo

print("Bien ahi")#Terminada la verificacion confirmar la respuesta
