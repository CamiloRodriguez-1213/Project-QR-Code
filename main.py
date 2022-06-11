from flask import Flask, jsonify,render_template,request,redirect,session,url_for
from controllers import loginUserController, restorePasswordController,validateTokenController,convertUrlShortToLargeController,userController
from controllers import qrCodeGeneratorController,showImagesController,optionsImageController,qrDecodeImageController,downloadImageController,newShortUrlController
from controllers import countQrAndShortenersUserController,showUrlsUserController,editimageController,deleteUrlUserController
from controllers.verify_loginController import verifyLogin
import webbrowser

app = Flask(__name__)
app.secret_key = 'fjifjidfjied5df45df485h48@'
@app.route("/", methods=["GET", "POST"])
def index():
    images = showImagesController.showImages()
    return render_template("index.html",images=images)
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if verifyLogin():
        images = showImagesController.showImagesUser()
        return render_template("/views/dashboard/dashboard.html",images=images)
    else:
        return redirect("signin")
@app.route("/myURls", methods=["GET", "POST"])
def myURls():
    if verifyLogin():
        urls = showUrlsUserController.showUrlsUserController()
        return render_template("/views/dashboard/urls-short.html",urls=urls)
    else:
        return redirect("signin")
@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        if loginUserController.signin(email,password) == True:
            return redirect("/")
        else:
            return render_template("/views/login/signin.html",email=email)
    return render_template("/views/login/signin.html")

@app.get("/logout")
def logout():
    if verifyLogin():
        session.clear()
    return redirect(url_for('signin'))
@app.route("/restorePassword", methods=["GET", "POST"])
def restorePassword():
    if request.method== 'POST':
        email=request.form['email']
        if restorePasswordController.restpass(email):
            return render_template("/components/alerts/alert.html")
    return render_template("/views/login/restorePassword.html")
@app.get("/newPassword/<id>/<token>")
def newPassword(id,token):
    if validateTokenController.valToken(id,token)==True:
        return render_template("/views/login/newPassword.html",id=id,token=token)
    else:
        return render_template("/components/alerts/alert.html")
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        if loginUserController.signup(name,email,password) == True:
            return redirect(url_for('signin',email=email))
        else:
            return render_template("/views/login/signup.html",email=email,name=name)
    return render_template("/views/login/signup.html")
@app.route("/authToken/<token>", methods=["GET", "POST"])
def authToken(token):
    if validateTokenController.valToken(token) == True:
        return render_template("/components/alerts/alert.html")
    return render_template("/components/alerts/alert.html")
@app.route("/decodeQR", methods=["GET", "POST"])
def decodeQR():
    if verifyLogin():
        if request.method == 'POST':
            fileProduct = request.files['image_decode']
            response = qrDecodeImageController.uploadImage(fileProduct)
            return render_template("/views/files_user/formDecodeImageQR.html",response=response)
        return render_template("/views/files_user/formDecodeImageQR.html")
    else:
        return redirect(url_for('signin'))
@app.route("/generateQR", methods=["GET","POST"])
def generateQR():
    if verifyLogin():
        if request.method == 'POST':
            data = request.form['url']
            description = request.form['description']
            size = request.form['size']
            color = request.form['color']
            qrCodeGeneratorController.QRCodeGenerator(data,description,color,size)
        return render_template("/views/files_user/formGenerateImageQR.html")
    else:
        return redirect(url_for('signin'))
@app.get("/editImage/<id>")
def editImage(id):
    images = showImagesController.showImagesEdit(id)
    return render_template("/views/products/formEditImage.html",images=images)
@app.post("/editImage/")
def editImagePost():
    if request.method == 'POST':
        id = request.form['id']
        estado = request.form['estado']
        nameProduct = request.form['name_product']
        editimageController.editImage(nameProduct,id,estado)
    return redirect(url_for('dashboard'))
@app.route("/changeStatus/<id>/<status>", methods=["GET","POST"])
def changeStatus(id,status):
    optionsImageController.changeImageStatus(id,status)
    return redirect(url_for('dashboard'))
@app.get("/deleteImage/<id>")
def deleteImage(id):
    optionsImageController.deleteImageUser(id)
    return redirect(url_for('dashboard'))
@app.get("/deleteUrl/<id>")
def deleteUrl(id):
    deleteUrlUserController.deleteUrl(id)
    return redirect(url_for('myURls'))
@app.get("/downloadImage/<url>")
def downloadImage(url):
    downloadImageController.downloadImage(url)
    if verifyLogin():
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('index  '))
@app.get("/viewImage/<url>")
def viewImage(url):
    webbrowser.open_new_tab('https://project-qr-code-flask.herokuapp.com/static/images/'+url)
    if verifyLogin():
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
@app.route("/shortener", methods=["GET", "POST"])
def shortener():
    return render_template("views/shorteners/short.html")
@app.route("/createShortener", methods=["GET", "POST"])
def createShortener():
    if request.method == 'POST':
        large_url=request.form['dirUrl']
        short_url = newShortUrlController.newShort(large_url)
        return render_template("views/shorteners/create.html",short_url=short_url,large_url=large_url)
    return render_template("views/shorteners/create.html")
@app.route("/short/<shortened>", methods=["GET","POST"])
def redirection(shortened):
    print(shortened)
    result = convertUrlShortToLargeController.convertUrl(shortened)
    
    return redirect(result[3], code=302)
@app.route("/myProfile", methods=["GET","POST"])
def myProfile():
    if verifyLogin():
        user = userController.userController()
        num_qr = countQrAndShortenersUserController.countAllQR()
        num_short = countQrAndShortenersUserController.countAllShort()
        return render_template("views/user/profile.html",user=user,num_qr=num_qr,num_short=num_short)
    else:
        return redirect(url_for('index'))
#app.run(debug=True)