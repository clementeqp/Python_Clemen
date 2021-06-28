# Como funciones pero devuelven varios valores a la vez
# Se almacenan en un objeto iterable , de uno en uno
# Entra en stanby cuando almacena un valor hasta que se solicita otro
# En lugar del return se pone un yield

"""
contador = 0
def generaNumerosPares(num):
    contador += 1
    numPar=0
    if contador*2<=num:
        numPar = contador*2
        print(contador*2)
    
    yield numPar
    
    """
    # Funcion 
    
def generarPares(limite):
    num=1
    numerosPares=[]
    while num<limite:
        numerosPares.append(num*2)
        num = num+1
    return numerosPares
print (generarPares(10))

print("-------------------------------------------------------------")
      
# Generador

def generaPares(limite):
    num=1
    
    while num<limite:
        yield num*2
        num = num+1
sucesionPares=generaPares(10)
"""
for i in sucesionPares:
    print(i)
    """
print(next(sucesionPares))
print(next(sucesionPares))
print(next(sucesionPares))
print(next(sucesionPares))

print("----------------------------------------------------------")

# Yield from, bucles anidados
# numero indeterminado de parametros en una tupla
def capitales_mundo(*ciudades):
    for capital in ciudades:
        #for letra in capital:
            #yield from letra
        yield from capital
capitales_devueltas=capitales_mundo("Berlin","Roma","Bogota", "Pekin", "Hanoi")

print(next(capitales_devueltas))
print(next(capitales_devueltas))
