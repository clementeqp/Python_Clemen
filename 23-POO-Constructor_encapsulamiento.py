class Persona():
    # _propiedad accesibble desde modulo y la herencia mas advertencia que bloqueo
    # __propiedad accesible solo de la clase
    # con __nombre No cambia el valor a Clemente
    
    __nombre=""
    apellido=""
    __edad=0
    genero="Sin definir"
    
    def __init__(self,__nombre, apellido,edad ,genero ):
        self.__nombre=__nombre
        self.apellido=apellido
        self.__edad=edad
        self.genero=genero
        
        
    def setEdad(self, edad):
        if 0<edad<100:
            self.__edad=edad
            print("Edad cambiada correctamente")
            return self.__edad
        else:
            return "Edad invalida"    
    
    def habla(self):
        return "La persona llamada ",self.__nombre ," esta hablando"
    
    def camina(self):
        return "La persona llamada ",self.__nombre ," esta caminando"
    
    def getDatos(self):
        return "Nombre: " + self.__nombre, "Apellido: " + \
            self.apellido,"Edad:",self.__edad ,"Genero:", self.genero
        
p1=Persona("Clemen","Quintana" ,42 ,"Macho" )

p1.__nombre="Clemente"

"""
Sin crear constructor

p1=Persona()
p1.__nombre="Clemen"
p1.apellido="Quintana"
p1.__edad=42
p1.genero="Macho alfa"
"""

print(p1.getDatos())

print(p1.setEdad(32))
print(p1.getDatos())

