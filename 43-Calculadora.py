from tkinter import *

raiz=Tk()
raiz.title("CalcuClemen")

miFrame=Frame(raiz)
miFrame.pack()
digitoDisplay=StringVar()
operacion=""
resultado=0


# Display
display=Entry(miFrame, textvariable=digitoDisplay, font="Arial 15")
display.grid(row=1,columnspan=4, pady=10)
display.config(bg="black", fg="#00db00", justify="right", width=15)

digitoDisplay.set("0")

# Tecleado numeros controlamos ceros izquieerda y comas mio
def pulsaTeclas2(num):
    global operacion
    
    digitoDisplay.set("")
    if num=="0" and digitoDisplay.get()=="0":
        digitoDisplay.set("0")
    elif num==".":
        if "." in digitoDisplay.get():
            pass
        else:
            digitoDisplay.set(digitoDisplay.get()+ num)
    else:        
        digitoDisplay.set(digitoDisplay.get()+ num)
        
        
def pulsaTeclas(num):
    global operacion
    
    if operacion != "":
        digitoDisplay.set(num)
        operacion=""
    else:
        if num=="0" and digitoDisplay.get()=="0":
            digitoDisplay.set("0")
        elif digitoDisplay.get()=="0" and num!=".":
            digitoDisplay.set(num)
        elif num==".":
            if "." in digitoDisplay.get():
                pass
            else:
                digitoDisplay.set(digitoDisplay.get()+ num)
        else:
            digitoDisplay.set(digitoDisplay.get()+ num)

""" # Funcion alternativa para la coma

def pulsa_coma():

    if "." in digito.Display.get():
        pass
    else:
        digitoDisplay.set(digitoDisplay.get()+ ".")

"""

    
# ------------- Funciones ---------------------------

def suma(num):
    global operacion, resultado
    if operacion !="suma":
        resultado+=float(num)
        operacion="suma"
        digitoDisplay.set(resultado)
            
def igual(num):
    global resultado
    resultado+=float(num)
    digitoDisplay.set(resultado)
    resultado = 0
    

    
    


#------- botonera ------------
# Fila 1

boton7=Button(miFrame, text="7", width=5, command=lambda:pulsaTeclas("7"))
boton7.grid(row=2, column=0)

boton8=Button(miFrame, text="8", width=5, command=lambda:pulsaTeclas("8"))
boton8.grid(row=2, column=1)

boton9=Button(miFrame, text="9", width=5, command=lambda:pulsaTeclas("9"))
boton9.grid(row=2, column=2)

botonDiv=Button(miFrame, text="/", width=5, )
botonDiv.grid(row=2, column=3)

# Fila 2
boton4=Button(miFrame, text="4", width=5, command=lambda:pulsaTeclas("4"))
boton4.grid(row=3, column=0)

boton5=Button(miFrame, text="5", width=5, command=lambda:pulsaTeclas("5"))
boton5.grid(row=3, column=1)

boton6=Button(miFrame, text="6", width=5, command=lambda:pulsaTeclas("6"))
boton6.grid(row=3, column=2)

botonMul=Button(miFrame, text="*", width=5)
botonMul.grid(row=3, column=3)

# Fila 3
boton1=Button(miFrame, text="1", width=5, command=lambda:pulsaTeclas("1"))
boton1.grid(row=4, column=0)

boton2=Button(miFrame, text="2", width=5, command=lambda:pulsaTeclas("2"))
boton2.grid(row=4, column=1)

boton3=Button(miFrame, text="3", width=5, command=lambda:pulsaTeclas("3"))
boton3.grid(row=4, column=2)

botonRes=Button(miFrame, text="-", width=5)
botonRes.grid(row=4, column=3)

# Fila 4
boton0=Button(miFrame, text="0", width=5, command=lambda:pulsaTeclas("0"))
boton0.grid(row=5, column=1)

botonComa=Button(miFrame, text=".", width=5, command=lambda:pulsaTeclas("."))
botonComa.grid(row=5, column=2)

botonIgual=Button(miFrame, text="=", width=5, command=lambda:igual(digitoDisplay.get()))
botonIgual.grid(row=5, column=0)

botonSum=Button(miFrame, text="+", width=5, command=lambda:suma(digitoDisplay.get()))
botonSum.grid(row=5, column=3)




raiz.mainloop()