# continue , hace que el bucle pase a la siguiente instruccion

for i in range(1,20):
    if i%2==0:
        continue
    print(i)
    
    
# Pass Cuando no queramos implementar aun el bucle o la clase 
nombre ="Clemente Quintana "
for i in nombre:
    pass

# La implementaremos luego
class EjemploClase():
    pass


# Else en for, solo entra en el else si recorre el bucle completo

email=input("Introduce tu email, por favor")

for i in email:
    if i=="@":
        arroba=True
        break
else:
    arroba=False
print(arroba)    
    
