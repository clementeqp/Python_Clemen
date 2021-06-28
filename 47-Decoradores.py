




# funcion decoradora
def sumar(f):
    #numero indeterminado de parametros **kwargs diccionarios
    def funcion_interna(*args, **kwargs):
        print(" ClementeQP: ".center(50, "-"))
        f(*args, **kwargs)
        print("Hecho ......")
    return funcion_interna

# funcion decoradora
def deco_sumar(f):
    
    def decora(*args):
        print(" ClementeQP: ".center(50, "-"))
        f(*args)
        print("Hecho ......")
    return decora
        
@deco_sumar
def suma(a,b):
    print(a+b)
suma(15,7)

@deco_sumar
def resta():
    print(15-7)
    
resta()

@sumar
def potencia(base, exponente):
    print(pow(base, exponente))
    
potencia(base=2, exponente=5)