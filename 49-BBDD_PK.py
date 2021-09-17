import sqlite3

# creamos la BBDD en la ruta especificada y conectamos
mi_conexion = sqlite3.connect("BBDD/Gestion_Pedidos.sqlite3")

mi_cursor = mi_conexion.cursor()
'''
mi_cursor.execute("""
    CREATE TABLE PRODUCTOS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_ARTICULO VARCHAR(40),
        PRECIO INTEGER,
        SECCION VARCHAR(20)
    )
    """)
'''
mis_productos = [
    ("AR01", "Camiseta", 50, "Moda"),
    ("AR02", "Jarron", 45, "Hogar"),
    ("AR03", "Chaqueta", 35, "Moda"),
    ("AR04", "Coche", 75, "Juguetes"),
    ("AR05", "Gorra", 15, "Deportes")
    ]




#mi_cursor.executemany("INSERT INTO Productos VALUES(?,?,?,?)",mis_productos)


mi_cursor.execute("INSERT INTO PRODUCTOS VALUES('AR02','zapatillas', 80, 'Deportes')")


mi_conexion.commit()

mi_conexion.close()
mi_conexion.close()
