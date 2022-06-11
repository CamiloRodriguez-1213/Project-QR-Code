import qrcode,time
from flask import flash,session
from models import createNewImageModel

def QRCodeGenerator(url,description,color,size):
    tiempo = str(time.time())
    qr = qrcode.QRCode(version= 1, box_size=size,border=5)
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color = color, back_color = 'white' )
    img.save('./static/images/'+tiempo+'.png')
    user = session['token']
    route = tiempo+'.png'
    if createNewImageModel.setNewImage(description,route,user,url):
            flash("La imagen ha sido guardada", "good")
    else:
        flash("Ha habido un error al subir la imagen", "wrong")
        flash("Vuelve a intentarlo", "wrong")