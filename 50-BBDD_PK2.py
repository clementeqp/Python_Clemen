import sqlite3

# creamos la BBDD en la ruta especificada y conectamos
mi_conexion = sqlite3.connect("BBDD/Gestion_Pedidos2.sqlite3")

mi_cursor = mi_conexion.cursor()

mi_cursor.execute("""
    CREATE TABLE PRODUCTOS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_ARTICULO VARCHAR(40),
        PRECIO INTEGER,
        SECCION VARCHAR(20)
    )
    """)

mis_productos = [
    ("Camiseta", 50, "Moda"),
    ("Jarron", 45, "Hogar"),
    ("Chaqueta", 35, "Moda"),
    ("Coche", 75, "Juguetes"),
    ("Gorra", 15, "Deportes")
    ]




mi_cursor.executemany("INSERT INTO Productos VALUES(null,?,?,?)",mis_productos)


mi_conexion.commit()

mi_conexion.close()
mi_conexion.close()
