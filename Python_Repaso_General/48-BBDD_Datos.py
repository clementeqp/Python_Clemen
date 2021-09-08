import sqlite3

# creamos la BBDD en la ruta especificada y conectamos
mi_conexion=sqlite3.connect("BBDD/BD_Python")

# creamos el cursor
mi_cursor=mi_conexion.cursor()
# creamos la tabla y luego comentamos para no repetir
#1 mi_cursor.execute("CREATE TABLE Productos (NARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

# insertamos elementos
#2 mi_cursor.execute("INSERT INTO Productos VALUES('Camiseta', 25, 'Moda')")

lista_productos=[
    ('Camisa', 30, 'Moda'),
    ('Patin',18, 'Deportes'),
    ('Jarrón', 75, 'Deccoracion')
]
#3 mi_cursor.executemany("INSERT INTO Productos VALUES(?,?,?)",lista_productos)

# leemos los datos
mi_cursor.execute("SELECT * FROM Productos")

lista_leidos=mi_cursor.fetchall()
print(lista_leidos)

for p in lista_leidos:
    print("Nombre:",p[0])

#confirmamos read no lo necesita
#mi_conexion.commit()

mi_cursor.close()
mi_conexion.close()