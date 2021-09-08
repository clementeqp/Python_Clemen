import io

fichero=open("PracticaDirectorio/clientes.txt", "r", encoding="utf-8")

lineas =fichero.readlines()

fichero.close()
clientes=[]

for linea in lineas:
    campos=linea.split(";")
    for i in range(0,6):
        cliente={"Codigo": campos[0], "Nombre":campos[1], "Direccion":campos[2], "Poblacion":campos[3],
                 "Telefono":campos[4], "Responsable":campos[5]}
        
    clientes.append(cliente)
    
for c in clientes:
    print("Codigo Articulo={} Nombre={} Direccion={} Poblacion={} Telefono={} Responsable={}"
          .format(c["Codigo"], c["Nombre"], c["Direccion"], c["Poblacion"], c["Telefono"], c["Responsable"] ))