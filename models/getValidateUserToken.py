from config.database import db
cursor = db.cursor()
def validateUserIdToken(id,token):
    try:
        id= int(id)
        if id>0:
            cursor.execute("SELECT * FROM users WHERE id_user = %s and token = %s",(id,token))
            myresult = cursor.fetchone()
            id = myresult[0]
            name = myresult[1]
            email = myresult[2]
            status = myresult[4]
            token = myresult[5]
            
            user = [id,name,email,status,token]
        return user
    except: 
        print("Error occured in getValidateUsertoken")