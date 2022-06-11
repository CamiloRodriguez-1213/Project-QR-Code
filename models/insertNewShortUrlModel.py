from config.database import db
from flask import session
cursor = db.cursor()
def setNewShort(short_url,large_url):
    try:
        if 'token' in session :
            tok = str(session['token'])
            cursor.execute("INSERT INTO shortener (short_url,user_id,large_url) VALUES (%s,%s,%s)",(short_url,tok,large_url))
        else:
            cursor.execute("INSERT INTO shortener (short_url,large_url) VALUES (%s,%s)",(short_url,large_url))
        db.commit()
        return True
    except:
        print("Error in insertNewShortModel")
        return False