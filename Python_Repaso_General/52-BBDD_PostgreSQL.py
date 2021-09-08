# conectar con PostgreSQL-----> Psycopg2
# estando en el directorio correcto pip install psycopg2

import psycopg2

mi_conexion=psycopg2.connect(host="localhost", database="Personas", user="postgres", password="admin", port="5433")
mi_cursor=mi_conexion.cursor()
mi_cursor.execute("INSERT INTO ALUMNOS VALUES ('Pepe', 'Martin')")

mi_conexion.commit()
mi_cursor.close()

mi_conexion.close()



