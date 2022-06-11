from models import insertNewShortUrlModel,generateNewTokenModel

def newShort(large_url):
    short_url = generateNewTokenModel.newToken()
    if insertNewShortUrlModel.setNewShort(short_url,large_url):
        return short_url