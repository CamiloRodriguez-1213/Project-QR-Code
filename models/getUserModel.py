from config.database import db
from flask import flash
cursor = db.cursor()
def user(email):
    try:
        cursor.execute("SELECT * FROM users WHERE email = '"+email+"'")
        myresult = cursor.fetchone()
        id = myresult[0]
        name = myresult[1]
        email = myresult[2]
        status = myresult[4]
        user = [id,name,email,status]
        return user
    except: 
        print("Error occured in getUserModel")
        return flash('El email '+email+' no está registrado','error')
