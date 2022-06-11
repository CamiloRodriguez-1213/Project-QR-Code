from flask import flash,session
from models import getUserModel
def userController():
    try:
        if 'token' in session :
            token = str(session['token'])
            user = getUserModel.userID(token)
            return user
    except:
        print("Error occured in userController")