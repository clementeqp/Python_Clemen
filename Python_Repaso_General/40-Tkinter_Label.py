from tkinter import *

root =Tk()

miFrame=Frame(root, width=500, height=450)

miFrame.pack()

# creamos un label y luego empaquetamos, adapta el 
# contenedor padre al tamaño del texto o usamos place(x=int, y=int)
miLabel1=Label(miFrame,text="Hola que tal estas .....",fg="red", font=("Arial", 20))
#miLabel1.pack()
miLabel1.place(x=150,y=0)


# imagenes, reconoce gif y png
miLogo=PhotoImage(file="images/python_img.png")
Label(miFrame, image=miLogo).place(x=150, y=150)



root.mainloop()