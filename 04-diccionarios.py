#diccionario={clave:valor, clave2:valor2, .....}

capitales={"España":"Madrid", "Francia":"Paris", "Italia":"Roma","Alemania":"Berlin"}

print(capitales)

# agregar valor
capitales["Colombia"]="Bogotáaaaaa"
print(capitales)

# modificar
capitales["Colombia"]="Bogotá"
print(capitales)

# borrar
del capitales["Colombia"]
print(capitales)

capitales[23]="M Jordan"
print(capitales)

#usando tuplas como clave

claveCapitales=["España", "Reino Unido", "Colombia", "Portugal"]

capitalesMundo={claveCapitales[0]:"Madrid", claveCapitales[1]:"Londres"}
print(capitalesMundo)

#ver las clave
print(capitalesMundo.keys())

#ver valores
print(capitalesMundo.values())

# longitud
print(len(capitalesMundo))

datosJordan={23:"Jordan","Nombre":"Michael","Equipo":"C Bulls", "anillos":[1991,1992,1993,1996,1997,1998]}

print(datosJordan["anillos"])
