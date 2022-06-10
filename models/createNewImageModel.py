from config.database import db
cursor = db.cursor()
def setNewImage(description,route,user,url):
    try:
        status = 'activo'
        cursor.execute("INSERT INTO images (description,route,user,status,url) VALUES (%s,%s,%s,%s,%s)",(description,route,user,status,url))
        db.commit()
        return True
    except:
        print("Error occured in setNewImageModel")
        return False