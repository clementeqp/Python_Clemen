import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import csv



class PostCrawled():

    def __init__(self, title, emoji, content, image):

        self.title = title
        self.emoji = emoji
        self.content = content
        self.image = image


class PostExtractor():

    def extraeInfo(self):

        urlBase="http://python.beispiel.programmierenlernen.io/index.php"
        posts=[]
        
        while urlBase!="":
            
            miDoc = requests.get(urlBase)
            
            docFinal = BeautifulSoup(miDoc.text, "html.parser")
            
            time.sleep(1)
            
            for card in docFinal.select(".card"):
                
                titulo=card.select(".card-title span")[1].text
                #solo selecciona la primera etiqueta
                emoji=card.select_one(".emoji").text
                content=card.select_one(".card-text").text
                image=urljoin(urlBase,card.select_one("img").attrs["src"])
                
                crawled=PostCrawled(titulo,emoji,content, image)
                #agregamos a cada vuelta el objeto a la lista Post[]
                posts.append(crawled)
                
            # subpaginas
            boton_next=docFinal.select_one(".navigation .btn")
            if boton_next:
                webx=urljoin(urlBase, boton_next.attrs["href"])
                urlBase=webx 
                print(webx)     
            else:
                urlBase="" #rompemos el bucle
              
            
        return posts
unPost=PostExtractor()

listaPosts=unPost.extraeInfo()

for l in listaPosts:
    print(l.emoji)
    print(l.title)
    print(l.image)
    print("")
    
    # sacar la ruta absoluta de la imagen
    # urllib.join
    
    # Subniveles
    # usamos un while pq no sabemos cuantas vueltas dara
    
    # guardar la info en un csv
with open('posts.csv', 'w', newline='', encoding='utf8') as csvfile:
    postwriter = csv.writer(csvfile, delimiter=';',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
    for mipost in unPost.extraeInfo():
        postwriter.writerow([mipost.emoji, mipost.title, mipost.image])
        
#leer csvfile

