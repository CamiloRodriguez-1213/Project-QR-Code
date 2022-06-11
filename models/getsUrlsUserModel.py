from config.database import db
cursor = db.cursor()
def getUrls(id):
    try:
        cursor.execute("SELECT * FROM shortener WHERE user_id = %s",(id,))
        myresult = cursor.fetchall()
        return myresult
    except: 
        print("Error occured in getUrlsUserModel")