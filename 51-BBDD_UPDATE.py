import sqlite3

# creamos la BBDD en la ruta especificada y conectamos
mi_conexion = sqlite3.connect("BBDD/Gestion_Pedidos2.sqlite3")

mi_cursor = mi_conexion.cursor()

# update
mi_cursor.execute("UPDATE PRODUCTOS SET PRECIO = 39 WHERE ID=2")

# Delete
mi_cursor.execute("DELETE FROM PRODUCTOS WHERE ID=3")

mi_conexion.commit()

mi_conexion.close()
mi_conexion.close()
