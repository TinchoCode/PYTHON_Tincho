a = 1
while a == 1: 
    vUno = int(input("Elegir un primer valor: "))
    vDos = int(input("Determinar valor a alcanzar: "))

    def bisection(a, b):
        lo, hi = min(a, b), max(a, b)
        count = 0
        while lo < hi:
            mid = (lo + hi) // 2
            print("Iteracion", count, ":", lo, ",", hi, "-> Medio:", mid)
            count += 1
            if mid < b:
                lo = mid + 1
            else:
                hi = mid
        print("Número de iteraciones requeridas: ", count)
        return lo

    result = bisection(vUno, vDos)
    print("Resultado es:", result, "\n")
    print("Quiere probar denuevo?")
    a = int(input("Si: 1 /// No: 0\n"))
