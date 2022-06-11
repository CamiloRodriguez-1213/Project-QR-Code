from flask import session
from models import getAllNumFilesModel

def countAllShort():
    try:
        if 'token' in session :
            token = str(session['token'])
            numShort = getAllNumFilesModel.getAllFilesUserShort(token)
            return numShort
    except:
        print("Error en CountQRAndShortenerController",'wrong')
def countAllQR():
    try:
        if 'token' in session :
            token = str(session['token'])
            numQR = getAllNumFilesModel.getAllFilesUserQr(token)
            return numQR
    except:
        print("Error en CountQRAndShortenerControllerQR",'wrong')