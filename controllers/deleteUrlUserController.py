from models import deleteUrlUserModel
from flask import session

def deleteUrl(id):
    try:
        user = session['token']
        deleteUrlUserModel.deleteUrl(id)
    except:
        print("Error occured in changeImageStatus")