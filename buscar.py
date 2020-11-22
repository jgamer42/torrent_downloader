import requests
from bs4 import BeautifulSoup

def busqueda_inicial(pelicula):
    salida = []
    data = requests.get(f"https://www.elitetorrent.in/?s={pelicula}&x=0&y=0").text
    parser = BeautifulSoup(data, 'html.parser')
    series_encontradas = parser.find_all("div",class_="meta")[0:5]
    for serie in series_encontradas:
        data = serie.find("a")
        salida.append(data["href"])
    return salida

def busqueda_detalle(datos):
    salida = []
    for pagina in datos:
        data = requests.get(pagina).text
        parser = BeautifulSoup(data, 'html.parser')
        titulo = parser.find("div",id="principal").find("h1").text.replace("Descargar ","").replace(" por torrent","")
        descarga = parser.find("div",class_="enlace_descarga").find_all("a")[1]["href"]
        info=parser.find("p",class_="descrip")
        description = info.find_all("span")
        i = 0
        if "Idioma:" in description[3].find("b").text:
        #print(description)
            peli={
                "id":i,
                "titulo":titulo,
                "fecha":description[0].text.replace("Fecha: ",""),
                "tamaño":description[1].text.replace("Tamaño: ",""),
                "genero":description[2].text.replace("Genero: ",""),
                "idioma":description[3].text.replace("Idioma: ",""),
                "formato":description[4].text.replace("Formato: ",""),
                "calidad":description[5].text.replace("Calidad: ",""),
                "descarga":descarga
            }
            salida.append(peli)
        i = i + 1
    return salida
