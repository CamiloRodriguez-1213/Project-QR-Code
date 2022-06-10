from config.database import db
cursor = db.cursor()
def changeStatus(id,status,user):
    try:
        if status == 'activo':
            estado= 'inactivo'
        if status == 'inactivo':
            estado= 'activo'
        cursor.execute("UPDATE images SET status = %s WHERE id_image = %s AND user = %s",(estado,id,user))
        db.commit()
        return True
    except:
        print("Error occured in updateStatusUSerModel")
        return False