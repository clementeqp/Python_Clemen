# While bucle indeterminado, no se sabe cuantas veces repetira

num=0
while num<5:
    print("Hola ", num)
    num += 1
print("Salimos del bucle")

num=0
while num!=5:
    num += 1
    print("Hola ", num)
   
print("Salimos del bucle")

edad=int(input("Introduce una edad: "))

while 0>edad or edad>100:
    print("Edad no valida")
    edad=int(input("Introduce una edad: "))
    
print("Gracias  %i es valida" %edad)