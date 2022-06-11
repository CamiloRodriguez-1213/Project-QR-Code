from config.database import db
from flask import flash
cursor = db.cursor()
def convertUrl(url_short):
    try:
        url_short= str(url_short)
        cursor.execute("SELECT * FROM shortener WHERE short_url = '"+url_short+"'")
        myresult = cursor.fetchone()
        return myresult
    except: 
        print("Error occured in convertUrlModel")
        
