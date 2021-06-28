# Actualizamos python : python -m pip install --upgrade pip
# instalamos el conector : pip install mysql-connector-python


# estando en el directorio correcto pip install psycopg2

import mysql.connector

mi_conexion=mysql.connector.connect(host="localhost", database="Personas", user="root", password="", port="3306")
mi_cursor=mi_conexion.cursor()
mi_cursor.execute("INSERT INTO ALUMNOS VALUES ('Pepe', 'Martin')")

mi_conexion.commit()
mi_cursor.close()

mi_conexion.close()