class Persona():
    
    def hablar(self):
        return "HAblo como las personas"
    
class Trabajador(Persona):
    
    def hablar(self):
        return "Hablo como un trabajador"
    
class Director(Trabajador):
    
    def hablar(self):
        return "Hablo como un Director"


def hazlesHablar(lista):
    
    for p in lista:
        print(p.hablar())
        
def hazleHablar(objeto):
    print(objeto.hablar())

    
Antonio=Persona()
Maria=Trabajador()
Ana=Director()

print(Antonio.hablar())
print(Maria.hablar())
print(Ana.hablar())

print("--------------------------------------")

listaPersonas=[Antonio, Ana, Maria]
hazlesHablar(listaPersonas)
print("--------------------------------------")
hazleHablar(Maria)