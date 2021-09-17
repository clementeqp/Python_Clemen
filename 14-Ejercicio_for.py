""" Python  Ejercicio bucle For I 
Ejercicio bucles y condicionales. Comparar listas
Crea una función que reciba dos listas por parámetros. La función debe comparar ambas listas,
devolviendo True si las listas son idénticas y False si no lo son
"""

def comparaListas(lista1, lista2):
    valor=False
    if lista1==lista2:
        valor=True
    return valor

def comparaListas2(lista1, lista2):
    if(len(lista1)!=len(lista2)):
        return False
    for i in range(0,len(lista1)):
        if(lista1[i]!=lista2[i]):
            return False
    return True


a=["Hola","2",3,4]
b=["Hola",2,3,4]

print(comparaListas(a, b))
print(comparaListas2(a, b))

print("----------------------------------------------------------------------")

"""
Python  Ejercicio bucle For II
Crea un programa de Python que pida 2 números por consola. El programa debe imprimir todos los números primos comprendidos entre los 2 números introducidos por consola.

Los números primos son aquellos que solo son divisibles por 1 y por ellos mismos.
"""
num1=int (input ("Introduce un primer numero:"))
num2=int (input ("Introduce un segundo numero:"))
isPrimo = False
if num1==num2:
    print("Los numeros son iguales. Introduzca diferentes")
    num1=int (input ("Introduce un primer numero:"))
    num2=int (input ("Introduce un segundo numero:"))

    
if num2<num1:
    num3=num1
    num1=num2
    num2=num3
    

if num1<num2:
    for i in range(num1, num2):
        for j in range(1,i):
            if i%j!=0:
                isPrimo=True
            else:
                if j!=1:
                    isPrimo = False
                    break
        if isPrimo==True or i==1:
            print(i)
            


print("-----------------------------------------------------------")

num1=int (input ("Introduce un primer numero:"))
num2=int (input ("Introduce un segundo numero:"))


def es_primo(numero):
    for n in range(2,numero):
        if numero % n == 0:
            return False 
    print(str(numero) + " es primo.")
    return True

for i in range(num1, num2):
    es_primo(i)    