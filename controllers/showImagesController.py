from flask import session
from models import getImagesModel
def showImages():
    try:
        images = getImagesModel.getImages()
        return images
    except:
        print("Error occured in showImages")
def showImagesUser():
    try:
        token = session['token']
        images = getImagesModel.getImagesUser(token)
        return images
    except:
        
        print("Error occured in showImagesUser")
def showImagesEdit(id):
    try:
        images = getImagesModel.getImagesId(id)
        return images
    except:
        print("Error occured in showImagesEdit")