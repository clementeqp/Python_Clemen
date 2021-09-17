#Metodos para manipular la clase String
nombre=input("Introduce tu nombre: ")

print(nombre.upper())
print(nombre.lower())
print(nombre.strip())
print(nombre.capitalize())
print(nombre.title())
print(nombre.isdigit())
print(nombre.isalnum())
print(nombre.count('a'))
print(nombre.replace('a', 'e'))

edad = input("Introduce tu edad: ")

while (edad.isdigit()==False):
    print("Valor incorrecto")
    edad = input("Introduce tu edad: ")
if (int(edad))<18:
    print ("No puedes pasar")
else:
  print("Puedes pasar")  