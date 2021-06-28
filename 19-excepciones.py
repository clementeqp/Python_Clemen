def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
    try:		
	    return num1/num2
    except ZeroDivisionError:
            print("Operacion no permitida")
            return "No se puede dividir por cero"
intentos =0        
while intentos<3:
    try:
        op1=(int(input("Introduce el primer número: ")))

        op2=(int(input("Introduce el segundo número: ")))
        break
        
    except ValueError:
        print("Numeros erroneos")
        intentos+=1
    
operacion=input("Introduce la operación a realizar (+,-,*,/): ")

print(op1,operacion,op2, " = ")		
    
if operacion=="+":
        print(suma(op1,op2))

elif operacion=="-":
        print(resta(op1,op2))

elif operacion=="*":
        print(multiplica(op1,op2))

elif operacion=="/":
        print(divide(op1,op2))

else:
        print ("Operación no contemplada")

print("Continuación de ejecución del programa")