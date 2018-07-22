from flask_rest_app.database import db
from flask_rest_app.database.models import Image
import shutil

def createImage(data):
   """Create an image object
   """
   imageUrl = data.get('imageUrl')
   imageObject = Image(imageUrl)
   db.session.add(imageObject)
   db.session.commit()
   return imageObject

def deleteImage(imageId):
   """Delete an Image object
   """
   imageObject = Image.query.filter(Image.id == imageId).one()
   try:
      shutil.rmtree(imageObject.imageLocalLocation)
   except Exception:
      print ("File %s failed to delete" % imageObject.imageLocalLocation)
   db.session.delete(imageObject)
   db.session.commit()