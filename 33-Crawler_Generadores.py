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
        #posts=[]
        contador=0
        
        while urlBase!="" and contador <=2:
            contador+=contador
            miDoc = requests.get(urlBase)
            
            docFinal = BeautifulSoup(miDoc.text, "html.parser")
            
            time.sleep(1)
            
            for card in docFinal.select(".card"):
                
                titulo=card.select(".card-title span")[1].text
                #solo selecciona la primera etiqueta
                emoji=card.select_one(".emoji").text
                content=card.select_one(".card-text").text
                image=urljoin(urlBase,card.select_one("img").attrs["src"])
                
                #crawled=PostCrawled(titulo,emoji,content, image)
                #agregamos a cada vuelta el objeto a la lista Post[]
                #posts.append(crawled)
                yield PostCrawled(titulo,emoji, content, image)
                
            # subpaginas
            boton_next=docFinal.select_one(".navigation .btn")
            if boton_next:
                webx=urljoin(urlBase, boton_next.attrs["href"])
                urlBase=webx 
                print(webx)     
            else:
                urlBase="" #rompemos el bucle
              
            
        #return posts
unPost=PostExtractor()

listaPosts=unPost.extraeInfo()
contador=0
for l in listaPosts:
    
    if contador ==12:
        break
    contador+=1
    print(l.emoji)
    print(l.title)
    print(l.image)
    print("")