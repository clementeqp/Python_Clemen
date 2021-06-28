"""Pide pais y ciudad y 
va almacenando en un diccionario la informacion las claves pais y las ciudades
en el campo valor con tipo lista sin repetir ni uno ni otro, 
cuando en pais escribes salir imprime el diccionario y sale"""

paises={}

pais=input("Introduce pais: ")

while pais!="salir":
    ciudad=input("Introduce la ciudad: ")
    lista_ciudades=paises.setdefault(pais, [ciudad])
    
    if lista_ciudades!=[ciudad]:
        paises[pais].append(ciudad)
        
    pais = input("Introduce el pais:")
    
print(paises)
