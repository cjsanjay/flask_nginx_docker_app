import os
import shutil

from flask_rest_app.app import initialize_app, app
from flask_rest_app.database import reset_database, IMAGE_LOCAL_LOCATION


def setupLocalImageDir(localDir):
    """
    """
    os.makedirs(localDir, exist_ok=True)

with app.app_context():
   reset_database()

setupLocalImageDir(IMAGE_LOCAL_LOCATION)