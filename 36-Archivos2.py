from io import open

archivo=open("archivo1.txt","r+", encoding="utf8")
# colocamos el cursor al final de la primera linea
#archivo.seek(len(archivo.readline()))

#print(archivo.read())

listaArchivo=archivo.readlines()

print(listaArchivo)

listaArchivo[1]="Otra linea nueva\n"

archivo.seek(0)
archivo.writelines(listaArchivo)

print(listaArchivo)

archivo.close()