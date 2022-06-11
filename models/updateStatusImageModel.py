from config.database import db
cursor = db.cursor()
def changeStatus(descripcion,id,status):
    try:
        if status == 'activo':
            estado= 'inactivo'
        if status == 'inactivo':
            estado= 'activo'
        estado=str(estado)
        cursor.execute("UPDATE images SET description = %s, status = %s WHERE images.id_image = %s",(descripcion,estado,id))
        db.commit()
        return True
    except:
        print("Error occured in updateStatusImageModel")
        return False

def changeStatusOne(id,status,user):
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