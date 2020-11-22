from qbittorrent import Client

def descargar(link):
    #aqui poner puerto 8080 o el puerto definido en qbit torrent
    cliente = Client("http://127.0.0.1:4000/")
    cliente.login("admin","adminadmin")
    #en savepath poner donde quiere guardar las peliculas
    cliente.download_from_link(link,savepath="/home/jaime/compartida/codigo/downloader/descargas/")