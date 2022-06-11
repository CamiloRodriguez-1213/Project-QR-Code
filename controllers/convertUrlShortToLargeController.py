from flask import flash
from models import getUrlLargeModel

def convertUrl(short_url):
    try:
        url = getUrlLargeModel.convertUrl(short_url)
        return url
    except:
        flash("No se ha podido encontrar el enlace",'wrong')
        print("No se ha podido encontrar el enlace")