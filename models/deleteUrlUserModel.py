from config.database import db
cursor = db.cursor()
def deleteUrl(id):
    try:
        id=int(id)
        cursor.execute("DELETE FROM shortener where id_shortener = %s",(id,))
        db.commit()
        return True
    except:
        return False