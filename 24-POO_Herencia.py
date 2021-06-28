class Persona():
    
    # Constructor de Persona con parametros
    def __init__(self, nombre, apellido, edad):
        
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
    
    def getDatosPersonales(self):
        return "Nombre: "+ self.nombre + " Apellido: " + self.apellido+ " Edad: " + str(self.edad)
    
    def habla(self):
        return "Estoy hablando"
    
    def piensa(self):
        return "Estoy pensando"

    def camina(self):
        return "Estoy comiendo"
    
    def come(self):
        return "Estoy comiendo"
    
# Clase estudiante hereda de Persona
class Estudiante(Persona): 
    
    # Constructor Estudiante
    def __init__(self, nombre, apellido, edad, escuela):
        # Llamada a constructor clase padre
        Persona.__init__(self,nombre, apellido, edad)
        self.escuela=escuela
        
    def getDatosPersonales(self):
        return super().getDatosPersonales() + " Escuela: " + self.escuela
    
    def estudia(self):
        return "Estoy estudiando"     
    
# Clase trabajador hereda de Persona
class Trabajador(Persona): 
    
    # Constructor Trabajador
    def __init__(self, nombre, apellido, edad, empresa):
        # Llamada a constructor clase padre
        Persona.__init__(self, nombre, apellido, edad)
        self.empresa=empresa
        
    def getDatosPersonales(self):
        return super().getDatosPersonales() + " Empresa: " + self.empresa
    
    def trabaja(self):
        return "Estoy trabajando"   

# Herencia Multiple
# Clase Director herede de trabajador y estudiante
# El orden importa, tiene preferencia la clase primera
class Director(Trabajador, Estudiante):
     
     def __init__(self, nombre, apellido, edad, empresa, escuela, bonus):
        Trabajador.__init__(self,nombre, apellido, edad, empresa)
        Estudiante.__init__(self,nombre, apellido, edad, escuela)
        self.bonus=bonus
        
        def getDatosPersonales(self):
            return super().getDatosPersonales() + " Bonus: " + self.Bonus
        def dirige(self):
            return "Estoy dirigiendo"

# Creamos un objeto Persona    
p1=Persona("Clemen","Quintana", 42)

# Hereda el constructor Persona
#e1=Estudiante("Sonia", "Rodriguez", 41)
e1=Estudiante("Sonia", "Rodriguez", 41, "IES Tatata")
p1.camina()

t1=Trabajador("Pedro", "Mesa", 41, "VDF")
d1=Director("Juan", "Diaz", 50, "Everis", "Ilerna", 1500)

e1.estudia()
e1.piensa()

print(p1.getDatosPersonales())

print(e1.getDatosPersonales())

print(d1.getDatosPersonales())