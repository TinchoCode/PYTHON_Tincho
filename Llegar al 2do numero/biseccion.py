#Este codigo solo sirve para llegar de un numero a otro de la forma "mas" rapida y eficiente, y mostrarte la cantidad de pasos que necesito.
#Ademas de implementar el metodo de Biseccion

a = 1
while a == 1: #Este loop es para poder hacerlo las veces que quieras
    vUno = int(input("Elegir un primer valor: "))
    vDos = int(input("Determinar valor a alcanzar: "))

    def bisection(a, b): #Asi se llama un metodo de busqueda para raices que se basa en la division y selecion de un lado   
        lo, hi = min(a, b), max(a, b) #Me fijo cual es menor (lo) y cual es mayor (hi) entre ambos valores 
        count = 0 #El contador
        while lo < hi: #Mientras que el "lo" sea menor a "hi"
            mid = (lo + hi) // 2 #Busca un punto medio (mid) entre ambos
            print("Iteracion", count, ":", lo, ",", hi, "-> Medio:", mid) #Impresion del numero de iteracion y los valores de "lo", "hi" y "mid"
            count += 1
            if mid < b: #Si "mid" es mayor a "b"
                lo = mid + 1 #"lo" va a ser igual a "mid" mas 1
            else: #Sino
                hi = mid #"hi" va a ser igual a "mid
        print("Iteracion", count, ":", lo, ",", hi) #Impresion de la ultima impresion, donde ambos numeros se encuentran 
        print("Número de iteraciones requeridas: ", count) #Simplemente el numero de iteraciones
        return lo

    result = bisection(vUno, vDos)
    print("Resultado es:", result, "\n")
    print("Quiere probar denuevo?")
    a = int(input("Si: 1 /// No: 0\n"))
