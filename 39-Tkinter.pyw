from tkinter import *

# creamos la raiz
raiz=Tk()

# modificar el titulo
raiz.title("AppClemenTk")

# redimensionado (0=falso, 1 verdadero) ancho alto
raiz.resizable(1,1)

# cambiar el icono
raiz.iconbitmap("images/python.ico")

# comenzar con un tamaño
raiz.geometry("700x700")

# creamos el frame dentro de la raiz
miFrame=Frame()
# empaquetamos luego hay que darle tamaño y color
miFrame.pack(pady="50px", padx="50px")

# Darle color
miFrame.config(bg="red")
#Darle tamaño
miFrame.config(width=600, height=600)

# color de fondo
raiz.config(bg="green")

# widgets de texto variable=Label(contenedor, opciones)





# mostramos la ventana
raiz.mainloop()



