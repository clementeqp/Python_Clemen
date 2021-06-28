import re 


cadena="Estoy trabajando con Python en domingo y semana Santa. El proximo domingo no trabajare"

print(re.search("domingo", cadena))
print(re.search("fruta", cadena))

busqueda="domingo"

if re.search(busqueda, cadena):
    print("Termino encontrado")
else:
    print("No se encontro el termino")
    
texto_encontrado=re.search(busqueda, cadena)

print(texto_encontrado.start())
print(texto_encontrado.end())
print(texto_encontrado.span()) # tupla

# todas las ocurrencias
print(re.findall(busqueda, cadena))
print(len(re.findall(busqueda, cadena)))

# metacaracteres
lista_nombres=["Antonio Banderas", "Juan Ruiz",
               "Clemen Clooney", "Tomas Crucero", "ejemplo"]
lista_terminos=["camion", "camión",
               "niño", "niña", "Antonio Resines"]
# ^ comienzan con


for n in lista_nombres:
    if re.findall("^Antonio", n):
        print(n)
        
# $ termina por
for n in lista_nombres:
    if re.findall("Ruiz$", n):
        print(n)
        
# caracteres comodin  [varias opciones], rangos [a-z], [a-z]$

for t in lista_terminos:
    if re.findall("cami[oó]n",t):
        print(t)
        
print("--------------------------")
for t in lista_terminos:
    if re.findall("niñ[a-u]",t):
        print(t)
        
print("--------------------------")

n1="Carmen López"
n2="Juan Díaz"
n3="Sancho Gracia"

c1="bbvbvvbvcb4v4bv4bvb6v4b4vb2vc2b123v64423vc2551bvcb6cv"
c2="gfdgdgf1gf231gfgf7g7fg9f87gdfgfgf323fd1gfdgfgfdg255gfdgfdgdfg"


# busca al principio solo
if re.match("sancho", n3,re.IGNORECASE):
    print("Encontrado")
else:
    print("No Encontrdado")
    
if re.match(".racia", n3):
    print("Encontrado")
else:
    print("No Encontrdado")
    
# Busca en todo
if re.search(".racia", n3):
    print("Encontrado")
else:
    print("No Encontrdado")
    
if re.search("255", c1):
    print("Encontrado")
else:
    print("No Encontrdado")