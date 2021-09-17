# Rastreadores crawlers
# instalar requests pip3 install requests

import requests

#miReq=requests.get("https://www.movistar.es/", auth=('user', 'pass')) Si hay usuario
miReq=requests.get("https://www.movistar.es/")

# print(miReq.status_code)
# print(miReq.headers)
print(miReq.text)

# extraemos la info y la analizaremos con beatufulsoup
# pip install beautifulsoup4

from bs4 import BeautifulSoup

miDoc="""
    <html>
    <style>
        .pImportante{
            color:red;
        }
    
    </style>
        <body>
            <p class='pImportante'>Primer parrafo</p>
            <p>Segundo parrafo</p>
            
            <a>Soy un vinculo</a>
        </body>
    </html>
"""

docFinal=BeautifulSoup(miDoc, "html.parser")

for parrafo in docFinal.find_all("p"):
    print(parrafo.attrs)
    print(parrafo.text)
   
#print(docFinal)