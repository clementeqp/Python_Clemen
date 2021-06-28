
#funcion sin parametros
def imprimeMensajes():

    print("Hola Caracola")
    print("Hola Caracolakjkjk")
    print("Hola Ckhjkjhkaracola")
    print("Holakjkjhk Caracola")
    print("Hkjkjhkola Carkjkjkacola")

imprimeMensajes()

print("EL programa ha termminado")

#funcion con parametros
def imprimeMensajes2(mensaje):
    print(mensaje)
    print(mensaje)

carta="Hola cariño que tal estas"
imprimeMensajes2(carta)

# return

def pasaMayus(texto):
    
    texto=texto.upper()
    
    return texto + "Se acabaron las funciones"

texto = "Hola titi que pasa"
print(pasaMayus(texto))

def suma(mensaje, n1, n2):
    return mensaje + str(n1+n2)

mensaje="La suma es: "
print(suma(mensaje, 5,7))

