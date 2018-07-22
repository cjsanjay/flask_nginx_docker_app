from flask_restplus import fields
from flask_rest_app.api.restplus import api

imageObject = api.model('Image', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of an Image'),
    'imageUrl': fields.String(required=True, description='Build Tag')
})

returnImageObject = api.model('Image', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of an Image'),
    'imageUrl': fields.String(required=True, description='Build Tag'),
    'imageLocalLocation': fields.String(required=True, description='Build Tag')
})