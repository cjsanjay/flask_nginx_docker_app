from datetime import datetime
import os

from flask_rest_app.database import db
from flask_rest_app.database import IMAGE_LOCAL_LOCATION

import urllib.request
import random

def downloadImage(imageUrl, imageLocalLocation):
   """Download image from @imageUrl and @return imageLocalLocation
   """
   fileName = random.randrange(1,10000)
   fullFileName = os.path.join(imageLocalLocation, str(fileName) + '.jpg')
   urllib.request.urlretrieve(imageUrl, fullFileName)
   return fullFileName

class Image(db.Model):
   """Image class
   """
   id = db.Column(db.Integer, primary_key=True)
   imageUrl = db.Column(db.String(80))
   imageLocalLocation = db.Column(db.String(80))

   def __init__(self, imageUrl):
      self.imageUrl = imageUrl
      self.imageLocalLocation = downloadImage(imageUrl, IMAGE_LOCAL_LOCATION)

   def __repr__(self):
      return '<Image URL %s:%s>' % (self.imageUrl, self.imageLocalLocation)
