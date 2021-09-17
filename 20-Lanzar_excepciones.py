import math

# Hace conversion implicita de entero a float
def calculaRaizCuadrada(numero):
    if numero<0:
        raise ValueError ("El numero no puede ser negativo")
    else:
        return math.sqrt(numero)

numeroUsuario=(int(input("Introduce un numero: ")))

try:
    print(calculaRaizCuadrada(numeroUsuario))
except:
    print("Numero incorrecto ")
print("Continua programa ...")