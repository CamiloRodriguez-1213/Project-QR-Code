from config.database import db
cursor = db.cursor()
def deleteUrl(id):
    try:
        cursor.execute("DELETE FROM shortener where id_shortener = '"+id+"'")
        db.commit()
        return True
    except:
        return False