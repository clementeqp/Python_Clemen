import math

print("Raiz cuadrada de valor numerico")

numero=int(input("Introduce un numero:"))

intentos = 1
while numero <0 and intentos <3:
    print("EL valor no puede ser negativo")
    numero=int(input("Introduce un numero:"))
    intentos+=1
    
if intentos==3:
    print("Has agotado tus intentos.")
else:
    print(math.isqrt(numero))
