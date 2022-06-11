from flask import flash,render_template,redirect,session
from werkzeug.security import check_password_hash,generate_password_hash
import re
from models import createUserModel, getEmailExistModel,generateNewTokenModel,createSendEmailModel
def signin(email,password):
    try:
        if email == '':
            flash('Correo electrónico','wrong')
        if password == '':
            flash('Contraseña','wrong')
        else:
            if getEmailExistModel.getSign(email):
                result = getEmailExistModel.getSign(email)
                checkPass = check_password_hash(result[3],password)
                if checkPass:
                    if result[4] == 'activo':
                        session['token'] = result[0]
                        session['user'] = result[1]
                        session['username'] = result[2]
                        return checkPass
                    else:
                        return flash("La cuenta aún no ha sido activada, revisa tu correo electrónico",'wrong')
                else:
                    flash('Usuario o contraseña incorrectos','wrong')
            else:
                flash("El usuario no existe",'wrong')
        return checkPass
    except:
        print("Error occured in signinUser")
def signup(name,email,password):
    try:
        isValid = True
        patternpw=re.compile('(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,20}')
        passwordval = re.search(patternpw, password)
        
        userAuth = False
        if name == '':
            isValid = False
            flash('* Nombre','wrong')
        if email == '':
            isValid = False
            flash('* Email','wrong')
        if not passwordval or password=='':
            isValid = False
            flash('* Contraseña:','wrong')
            flash('El campo contraseña debe contener un mínimo de 8 caracteres, un máximo de 20, letras, (minúsculas y MAYÚSCULAS) y Números','wrong')
        if isValid == False:
            return render_template("/views/login/signup.html", name = name, email = email)
        else:
            result = getEmailExistModel.getSign(email)
            if result:
                flash("El email "+email+" ya se encuentra registrado",'wrong')
                return redirect('/signup')
            else:
                passwordCod=generate_password_hash(password)
                token = generateNewTokenModel.newToken()
                
                asunto = "Hola "+name+", te damos la bienvenida a nuestra página"
                content = "<h2>Bienvenido a My-App "+name+" </h2>\n<h4>Activa tu cuenta dando clic al siguiente botón </h4>\n<a target='_blank' href='https://project-qr-code-flask.herokuapp.com/authToken/"+token+"'><button>Activa tu cuenta</button></a>"
                emailReceived = createSendEmailModel.sendMail(asunto,email,content)
                emailReceived = True
                if emailReceived == True:
                    print("Correo enviado")
                    createUserModel.setUserInactive(name,email,passwordCod,token)
                    userAuth = True
        return userAuth
    except:
        print("Error occured")
        flash("Ha habido un problema al enviar el correo",'wrong')
      

    