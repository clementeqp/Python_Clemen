from tkinter import *
from tkinter import messagebox

raiz=Tk()


miFrame=Frame(raiz, width=1000, height=550)
miFrame.pack()

miVariable=StringVar()

# creamos una entrada de texto en miFrame
cuadroTexto=Entry(miFrame, textvariable=miVariable)
cuadroTexto.grid(row=0, column=1, padx=15, pady=5, sticky="w")

# nombre
nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0,column=0)

# apellidos 
apellidosLabel=Label(miFrame, text="Apellidos: ")
apellidosLabel.grid(row=1,column=0, sticky="w")

cuadroTexto2=Entry(miFrame)
cuadroTexto2.grid(row=1, column=1, padx=15, pady=5, sticky="w")

# contraseña
contraLabel=Label(miFrame, text="Contraseña: ")
contraLabel.grid(row=2,column=0, sticky="w")

cuadroContra=Entry(miFrame)
cuadroContra.grid(row=2, column=1, padx=15, pady=5, sticky="w")
cuadroContra.config(show="*")

# direcion
direccionLabel=Label(miFrame, text="Direccion: ")
direccionLabel.grid(row=3,column=0, sticky="w")

cuadroTexto3=Entry(miFrame)
cuadroTexto3.grid(row=3, column=1, padx=15, pady=5, sticky="w")


# mail
mailLabel=Label(miFrame, text="Mail: ")
mailLabel.grid(row=4,column=0, sticky="w")

cuadroTexto4=Entry(miFrame)
cuadroTexto4.grid(row=4, column=1, padx=15, pady=5, sticky="w")

# Comentarios cuadro de texto text area
comentariosLabel=Label(miFrame, text="Comentarios: ")
comentariosLabel.grid(row=5,column=0, sticky="nw")

cuadroTexto5=Text(miFrame, width=20, height=10)
cuadroTexto5.grid(row=5, column=1, padx=15, pady=5)
comentario=StringVar()

# crear un boton

# funcion que hara el boton

def funcionBoton():
    comentario=cuadroTexto.get()
    messagebox.showinfo("Comentario", comentario)
    miVariable.set("Clemen")
    
    
botonEnviar=Button(raiz, text="Enviar", command=funcionBoton)
botonEnviar.pack()

# barra de desplazamiento
miBarra=Scrollbar(miFrame, command=cuadroTexto5.yview)
miBarra.grid(row=5, column=2, sticky="nsew")

# barra marque posicion
cuadroTexto5.config(yscrollcommand=miBarra.set)



raiz.mainloop()