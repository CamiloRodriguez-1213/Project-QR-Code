from flask import flash,session
from pyzbar.pyzbar import decode
from PIL import Image
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
def uploadImage(fileProduct):
    try:
        if fileProduct and verifyExtend(fileProduct.filename):
            decoded = decode(Image.open(fileProduct))
            data = decoded[0].data.decode('utf-8')
            return data
        else:
            flash('Tipo de archivo no admitido','wrong')
    except:
        print("Error occured in uploadImage")
def verifyExtend(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS