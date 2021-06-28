

capitales={"China":"Pekín", "India":"Nueva Delhi", "Indonesia":"Yakarta", "Japón":"Tokyo"}
for c in capitales:
    valor=capitales[c]
    print((c + " ").ljust(25,"-"),valor)
    
# imprimimos el diccionario    
print(capitales.items())

# con for

for c,v in capitales.items():
    print((c + " ").ljust(25,"-"),v)
    