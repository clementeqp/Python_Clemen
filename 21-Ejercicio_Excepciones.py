def pideNombres():
    nombres=[]
    for i in range(0,3):
        nombre=input("Introduce un nombre propio: ")
        for n in nombres:
            if n == nombre:
                raise ValueError ("Nombre repetido")
                break           
        nombres.append(nombre)
    return nombres    
try:
    nombres =pideNombres()
except ValueError:
    print("Nombre repetido")
for nombre in nombres:
    print(nombre)


print("-----------------------------------------------------------")


nombres=[]

def agregarNombres(lista, nombre):
    try:
        if nombre in lista:
            raise ValueError
        else:
            lista.append(nombre)
    except ValueError:
        print("Ese nombre ya existe", nombre)
introducidos =0

while introducidos<5:
    nombre=input("Introduce un nombre: ")
    agregarNombres(nombres, nombre)
    introducidos+=1        
    
print(nombres)