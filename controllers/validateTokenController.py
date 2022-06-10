from flask import flash
from models import getTokenUserModel, updateStatusUserModel,getValidateUserToken
def valToken(token):
    value =False
    result = getTokenUserModel.getToken(token)
    if not result == None:
        idUser = result[0]
        if updateStatusUserModel.setnewToken(idUser):
            flash('Su cuenta ha sido activada correctamente','good'),flash('Cierre la pestaña','good')
            value = True
    else:
        value = False
        flash('El token ya ha sido utilizado','wrong'),flash('Cierre la pestaña','wrong')
    return value
def validateIdToken(id,token):
    user = getValidateUserToken.validateUserIdToken(id,token)
    if user == None or user[4] == 'null':
        flash('La dirección url es incorrecta o ya se ha utilizado este token','wrong')
        return False
    else:
        return True