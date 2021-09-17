# nombreLista=[entero, "elem2", elem3.......] Diferente tipo

from typing import ChainMap


trabajadores=["Ana", "Maria", "Antonio","Clemen"]

print(trabajadores)

#tamaño lista
print(len(trabajadores))

#invertir lista
trabajadores.reverse()
print(trabajadores)

#añadir elementos
trabajadores.append(5)
print(trabajadores)

#unir listas
jefes=["Capi","Capo"]
trabajadores.extend(jefes)
print(trabajadores)

#unir con +
print(trabajadores + jefes)

#rangos
print(trabajadores[2])
print(trabajadores[-1])
print(trabajadores[2:3])
print(trabajadores[:5])
print(trabajadores[2:])
print(trabajadores)

#eliminar un elemento
trabajadores.remove('Capi')
print(trabajadores)

del trabajadores[0]
print(trabajadores)

#indice de un elemento
print(trabajadores.index('Capo'))

print(trabajadores.count(5))