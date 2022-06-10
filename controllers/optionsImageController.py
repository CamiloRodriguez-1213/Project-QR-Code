from models import getImagesModel,deleteImageModel,updateStatusImageModel
from os import remove,path
from flask import flash, session
def deleteImageUser(id):
    try:
        result = getImagesModel.getImagesId(id)
        name = result[2]
        if path.exists("./static/images/"+name+""):
            if deleteImageModel.deleteImage(id):
                remove("./static/images/"+name+"")
                flash('Se ha eliminado la imagen correctamente','good')
            else:
                flash('No se ha podido eliminar la imagen','wrong')
    except:
        print("Error occured in deleteImageUser")
def changeImageStatus(id,status):
    try:
        user = session['token']
        updateStatusImageModel.changeStatus(id,status,user)
    except:
        print("Error occured in changeImageStatus")
