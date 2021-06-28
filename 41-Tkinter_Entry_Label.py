from tkinter import *

raiz=Tk()


miFrame=Frame(raiz, width=1000, height=550)
miFrame.pack()
# creamos una entrada de texto en miFrame
cuadroTexto=Entry(miFrame)

#cuadroTexto.place(x=50, y=50)
# lo hacemos con grid
cuadroTexto.grid(row=0, column=1)

# etiqueta
nombreLabel=Label(miFrame, text="Nombre: ")
# nombreLabel.place(x=50, y=50)
# con grid, sticky alinea n,s,w,e.se,sw....
nombreLabel.grid(row=0,column=0, sticky="w")

# etiqueta
apellidosLabel=Label(miFrame, text="Apellidos: ")
# nombreLabel.place(x=50, y=50)
# con grid
apellidosLabel.grid(row=1,column=0, sticky="w")
#cuadroTexto.place(x=50, y=50)
# lo hacemos con grid
cuadroTexto2=Entry(miFrame)
cuadroTexto2.grid(row=1, column=1)

# etiqueta
direccionLabel=Label(miFrame, text="Direccion: ")
# nombreLabel.place(x=50, y=50)
# con grid
direccionLabel.grid(row=2,column=0, sticky="w")
#cuadroTexto.place(x=50, y=50)
# lo hacemos con grid
cuadroTexto3=Entry(miFrame)
cuadroTexto3.grid(row=2, column=1)


# etiqueta
mailLabel=Label(miFrame, text="Mail del usuario actual: ")
# nombreLabel.place(x=50, y=50)
# con grid
mailLabel.grid(row=3,column=0, sticky="w")
#cuadroTexto.place(x=50, y=50)
# lo hacemos con grid
cuadroTexto4=Entry(miFrame)
cuadroTexto4.grid(row=3, column=1)
raiz.mainloop()