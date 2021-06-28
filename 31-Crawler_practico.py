from bs4 import BeautifulSoup
import requests

miDoc=requests.get("http://python.beispiel.programmierenlernen.io/index.php")

docFinal=BeautifulSoup(miDoc.text, "html.parser")

iconos=docFinal.select(".emoji")
## Acceder al elemento primero de la clase emoji
#print(iconos[0].text)

title=docFinal.select(".card-title span")

print(title[1].text)
print(title[0].text)

# acceder al texto

text = docFinal.select(".card-text")

print(text[2])

for t in text:
    print(t.text)
    print("--------------------------------------------")
    
    
# acceder a la imagen

image = docFinal.select(".card-block img")

for i in image:
    
    print(i.attrs["src"]) 