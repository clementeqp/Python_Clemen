# creamos un setup.py en la raiz

# Desde el directorio python setup.py sdist
# instalarlo pip3 install nombreDelPaqueteDistribuible y se añadira a la biblioteca de python
# podemos importar paquetes y trabajaremos mas comodo

import csv
with open('ejemplo_csv.csv', newline='') as csvfile:
    miCsv = csv.reader(csvfile, delimiter=',')
    for linea in miCsv:
        print(' '.join(linea))


