from config.database import db
cursor = db.cursor()
def getImages():
    try:
        cursor.execute("SELECT * FROM images,users WHERE images.status= 'activo' AND images.user = users.id_user")
        myresult = cursor.fetchall()
        return myresult
    except: 
        print("Error occured in getImagesModel")
def getImagesUser(token):
    try:
        token = str(token)
        cursor.execute("SELECT * FROM images WHERE images.user = '"+token+"' ")
        myresult = cursor.fetchall()
        return myresult
    except: 
        print("Error occured in getImagesModeluser")
def getImagesId(id):
    try:
        cursor.execute("SELECT * FROM images WHERE images.id_image = '"+id+"' ")
        myresult = cursor.fetchone()
        return myresult
    except: 
        print("Error occured in getImagesModelID")