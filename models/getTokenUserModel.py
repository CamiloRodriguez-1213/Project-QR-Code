from config.database import db
from flask import flash
cursor = db.cursor()
def getToken(token):
    try:
        cursor.execute("SELECT * FROM users WHERE token = '"+token+"'")
        myresult = cursor.fetchone()
        return myresult
    except: 
        print("Error occured in getTokenUserModel")