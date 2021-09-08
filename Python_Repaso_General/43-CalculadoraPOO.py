from tkinter import *

raiz=Tk()

class Calculadora():
    def __init__(self, ventana):
        
        self.ventana=ventana
        self.ventana.title("Calcu POO")
        
        # Agregar display
        self.display=Entry(ventana, font="Arial 15")
        # ubicar display
        self.display.grid(row=1,columnspan=4, pady=10)
        self.display.config(bg="black", fg="#00db00", justify="right", width=25)
        
        # Crear botones
        botones=[]
        for i in range(0,10):
            boton=self.colocar_boton(i)
            botones.append(boton)
        boton_mas=self.colocar_boton("+", mostrar=False)   
        
        
        contador=0
        for fila in range(2,6):
            for col in range(4):
                botones[contador].grid(row=fila, column=col)
                contador+=1
        
        
    def colocar_boton(self, valor, mostrar=True, ancho=9, alto=1):
        return Button(self.ventana, text=valor, width=ancho, height=alto,
                      font=("Helvetica", 10), command=lambda:self.pulsaciones_teclas(valor, mostrar))       


mi_calculadora= Calculadora(raiz)





raiz.mainloop()