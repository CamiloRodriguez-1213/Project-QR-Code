from flask import flash, session
from models import getsUrlsUserModel

def showUrlsUserController():
    try:
        token = session['token']
        urls = getsUrlsUserModel.getUrls(token)
        return urls
    except:
        print("Error occured in showUrlsUserController")
        flash('No tiene urls registradas','wrong')