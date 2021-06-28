"""Se trata de elaborar un programa que genere un número aleatorio entre 1 y 100. Para ello
debemos importar el módulo random y utilizar la instrucción random.randint(1,100). Esta
instrucción genera un número entero entre 1 y 100.
A continuación, se le pide al usuario que introduzca un número por consola entre 1 y 100. Si el
número introducido por el usuario es menor, se imprime en consola un mensaje indicando que
el número aleatorio es mayor que el introducido por él. Si el número introducido por el usuario
es mayor que el aleatorio, se imprime un mensaje indicando que el número aleatorio es menor
que el introducido por él. Después de indicar si es mayor o menor, se vuelve a pedir al usuario
que introduzca un número entre 1 y 100.
Se trata de averiguar cuál es el número aleatorio generado por el programa a base de ir
aproximándonos intento tras intento, y hacerlo en el menor número de intentos posibles así que
también debemos controlar cuántos intentos consume el usuario para adivinar el número
aleatorio generado por el programa.
Cuando el usuario averigüe finalmente el número aleatorio, el programa imprimirá en consola
“Correcto. Has utilizado…” y el nº de intentos consumidos"""
import random

numSecreto = random.randint(1,100)
num=0
contador = 0

while num!=numSecreto and contador<10:
    print("LLevas ", contador, " intentos.")
    num=int(input("Que numero he pensado:"))
    contador+=1
    if num<numSecreto:
        print("Lo siento el numero es mayor, vuelve a intentarlo")
    elif num>numSecreto:
        print("El numero secreto es menor")
    else:
        print("Has acertado, el numero secreto era " + str(numSecreto) 
              + " y lo has acertado en " + str(contador) + " intentos.")
if contador==10:
    print("Lo siento, has agotado los intentos.")
else:
    print("Hasta luego campeón")