import logging.config

import os
import shutil
from flask import Flask, Blueprint
from flask_rest_app import settings
from flask_rest_app.api.imageops.endpoints.image import ns as imageOps_namespace
from flask_rest_app.api.restplus import api
from flask_rest_app.database import db, IMAGE_LOCAL_LOCATION


def configure_app(flask_app):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP

def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(imageOps_namespace)
    flask_app.register_blueprint(blueprint)

    db.init_app(flask_app)

app = Flask(__name__)
log = logging.getLogger(__name__)
initialize_app(app)

def main():
    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(host='0.0.0.0', port=8080)


if __name__ == "__main__":
    main()
