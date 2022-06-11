import requests
from flask import flash
def downloadImage(url):
    try:
        url_imagen = 'https://project-qr-code-flask.herokuapp.com/'+url # El link de la imagen
        nombre_local_imagen = './static/newImages/download'+url # El nombre con el que queremos guardarla
        imagen = requests.get(url_imagen).content
        with open(nombre_local_imagen, 'wb') as handler:
            handler.write(imagen)
        flash('Se ha descargado la imagen correctamente','good')
    except:
        print("Error al descargar la imagen")
        flash('Se ha descargado la imagen correctamente','wrong')