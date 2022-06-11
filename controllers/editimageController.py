from config.database import db
from flask import flash,session
from models import updateStatusImageModel,deleteImageModel,getImagesModel
from os import remove
from PIL import Image
from os import path
cursor = db.cursor()

def editImage(descripcion,id,estado):
    try:
        if updateStatusImageModel.changeStatus(descripcion,id,estado):
            flash("La imagen ha sido guardada", "good")
        else:
            flash("Ha habido un error al subir la imagen", "wrong")
            flash("Vuelve a intentarlo", "wrong")
            #convertir = datetime.fromtimestamp(tiempo)
    except:
        print("Error occured in uploadImage")
def deleteImageUser(id):
    try:
        result = getImagesModel.getImagesId(id)
        print(result)
        name = result[2]
        if path.exists("./static/images/"+name+""):
            if deleteImageModel.deleteImage(id):
                print(name)
                remove("./static/images/"+name+"")
                
                flash('Se ha eliminado la imagen correctamente','good')
            else:
                flash('No se ha podido eliminar la imagen','wrong')
    except:
        print("Error occured in deleteImageUser")
