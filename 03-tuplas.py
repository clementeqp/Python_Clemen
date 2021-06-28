#nombre=(elem1, elem2,elem3)

misDatos=("Clemen", 15,8,1980)
print(misDatos)

#conversion tupla en lista y viceversa
misDatosLista=list(misDatos)
print(misDatosLista)
misDatosLista=tuple(misDatosLista)
print(misDatosLista)

#Buscar un elemento
print(15 in misDatos)

#contar veces de un elemento
print(misDatos.count("Clemen"))

#elementos total
print(len(misDatos))

#desempaquetado de tupla
nombre, dia, mes, anyo=misDatos
print(nombre)

#no permiten agregar ni eliminar elementos, son inmutables






