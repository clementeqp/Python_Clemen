# Modulo OS

import os
import io

# Crear una carpeta en el directorio actual

#os.makedirs("Carpeta_Python_Prueba")

# Crear directorio
#os.makedirs("PracticaDirectorio2")

#movernos
#os.chdir("PracticaDirectorio2")

#archivoExt=open("Ejemplo2.docx", "w")

#archivoExt.write("Testo de Ejemplo2...")


# renombrar vamos al direcorio
#os.rename("Ejemplo.txt", "Archivo a eliminar.txt")

# eliminar
#os.remove("Archivo a eliminar.txt")

# eliminar directorio con contenido no deja
#os.rmdir("PracticaDirectorio2")
# vamos al directorio borrmaos contenido salimos del drectorio y eliminamos
# luego el directorio
os.chdir("PracticaDirectorio2")

#os.remove("Ejemplo2.docx")
#podemos usar un bucle y recorrer los archivos , buscarlos, borrarlos

os.chdir("../")

os.rmdir(("PracticaDirectorio2"))


print(os.getcwd())

# imprimir listado directorio
print(os.listdir("./"))

# Imprimir ruta actual
print(os.getcwd())

# Mover a un directorio
#os.chdir("Carpeta_Python")

