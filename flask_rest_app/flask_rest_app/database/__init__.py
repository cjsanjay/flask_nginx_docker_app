import os
from flask_sqlalchemy import SQLAlchemy
import shutil

db = SQLAlchemy()


def reset_database():
    from flask_rest_app.database.models import Image
    db.drop_all()
    db.create_all()

IMAGE_LOCAL_LOCATION = os.path.join(os.getcwd(), "storedImages")
