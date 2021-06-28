# Importamos nuestro modulo de funciones matematicas

# crear un paquete haremos una carpeta con un archivo __init__.py y los modulos que queramos

import Modulos.funciones_matematicas

Modulos.funciones_matematicas.sumar(8,9)

from Modulos.funciones_matematicas import sumar, dividir

sumar(8,7)

from Modulos.funciones_matematicas import *

dividir(27,9)
