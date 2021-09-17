

def func_area_triangulo(base, altura):
    return base*altura/2


triangulo1=func_area_triangulo(3,6)

print(triangulo1)

area_triangulo=lambda base, altura : base*altura/2

print(area_triangulo(3,6))


calculo_cubo=lambda base: base**3
print(calculo_cubo(5))

calculo_cubo=lambda base,exp: base**exp
print(calculo_cubo(5,3))


print("------------------------------------------")

comision=lambda num : "!! "+ str(num) +" €"
print(comision(500))

comision_formato=lambda comision:" ¡ {} ! € ".format(comision).center(50,"-")

comision_clemen=1500
print(comision_formato(comision_clemen))

print("-------------------------------")

mi_lista=[5,2,9,7,5,6,48,1,4,23,14,21,87]
mi_lista2=[(2,3), (5,7),(9,2),(3,8)]


print(mi_lista)
mi_lista.sort(reverse=True)
print(mi_lista)

def ordena_lista(t): 
    return t[0]+t[1]

mi_lista2.sort(key=ordena_lista, reverse=True)

print(mi_lista2)

print("---------------------------------")

mi_lista2.sort(key=lambda t:t[0]-t[1])
print(mi_lista2)

print("---------------------------------")

musicos =["Paul McCartney","Bruce Springsteen", "Tina Turner", "Justin Bieber"]

def ordena_musicos(m):
    return m.split()[1]
print(musicos)
musicos.sort(key=ordena_musicos)
print(musicos)


musicos.sort(reverse=True)
print(musicos)

musicos.sort(key=lambda m:m.split()[1])
print(musicos)