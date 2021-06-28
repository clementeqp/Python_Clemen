# creamos una clase

class Coche():
    # Propiedades
    ruedas=4
    largoChasis=260
    anchoChasis=130
    arrancado=False
    
    # Metodos, siempre recibiran el parametro self al menos
    def arrancar(self):
        self.arrancado=True
        
    def estadoCoche(self):
        if self.arrancado:
            return "El coche esta arrancado...."
        return "El coche no esta arrancado ...."
    
    def parar():
        pass
    
    def girar():
        pass
    
# Instanciamos un objeto coche
mazda=Coche()

audi=Coche()

print("Tu coche tiene" , mazda.ruedas,"ruedas")
print(audi.estadoCoche())
audi.arrancar()
print(audi.estadoCoche())