# Metodo __str__()

class Persona():
    
    almacen_datos=[] 
    
    # con ** esperara un diccionario, con * una lista
    def __init__(self, *datos):
        for d in datos:
            self.almacen_datos.append(d)
    # Con este metodo modificamos el print del objeto __str__()
    def __str__(self):
        return "Nombre: " + self.almacen_datos[0] + "\nApellido: " + self.almacen_datos[1] +\
            "\nEdad: " + str(self.almacen_datos[2])
    
    
    # Hace lo mismo que str pero es mucho mas preciso 
    # identifica al objeto de forma inequivoca    
    def __repr__(self):
        return "Nombre: " + self.almacen_datos[0] + "\nApellido: " + self.almacen_datos[1] +\
            "\nEdad: " + str(self.almacen_datos[2])
            
    
p1=Persona("Clemen","Quintana", 42)
p2=Persona("Clemen","Quintana", 42, "Informatico", "Hombre")
print(p1)

print("\n-----------------------------------------------------\n")
# __repr__()   representacion en formato texto de nuestro objeto

import datetime


hoy = datetime.date.today()

print(repr(hoy))
print(str(hoy))

print("\n-----------------------------------------------------\n")

# __len__()
class Agenda():
        
    def __init__(self):
        self.miAgenda={}
        
    def agregarPersonas(self, nombre, telefono):
        self.miAgenda[nombre]=telefono
        
    def __len__(self):
        return len(self.miAgenda)
    
agenda=Agenda()

agenda.agregarPersonas("Clemen", 654879123)
agenda.agregarPersonas("Maria", 878945645)
agenda.agregarPersonas("Ana", 123456789)

# no funciona si no sobreescribimos el __len__()
print(len(agenda))    
    