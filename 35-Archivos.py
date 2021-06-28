# Trabajaremos con la clase io

from io import open

# 3 parametros: nombre, modo(w,r,a), codificacion opcional
# archivo=open("archivo1.txt", "w", encoding="utf8")
#archivo=open("archivo1.txt", "a", encoding="utf8")
archivo=open("archivo1.txt", "w", encoding="utf8")

archivo.write("Hola\n")
archivo.write("Que tal estas")

archivo.write("\nGuardando....")
# read(10 lee hasta el caracter 10)
#informacion=archivo.read()

#print(informacion)




# readLine/s lee linea a linea

#info_linea=archivo.readline()
# retorna el cursor al caracter 0
#archivo.seek(0) 
#info_lineas=archivo.readlines()


archivo.close()


# El cursor queda donde termina de leer
#print(info_linea)



#print(info_lineas[0])