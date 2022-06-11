from config.database import db
cursor = db.cursor()
def getAllFilesUserShort(id):
    try:
        cursor.execute("SELECT count(*) AS allcount FROM shortener where user_id = %s",(id,))
        totalRegistro = cursor.fetchone()
        return totalRegistro
    except:
        print("Error occured in getAllNumFilesModel")
def getAllFilesUserQr(id):
    try:
        cursor.execute("SELECT count(*) AS allcount FROM images where user = %s",(id,))
        totalRegistro = cursor.fetchone()
        return totalRegistro
    except:
        print("Error occured in getAllNumFilesModelShort")