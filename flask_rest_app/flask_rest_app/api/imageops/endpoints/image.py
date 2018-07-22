import logging

from flask import request
from flask_restplus import Resource
from flask_rest_app.api.imageops.dboperation import createImage
from flask_rest_app.api.imageops.dboperation import deleteImage
from flask_rest_app.api.imageops.serializers import (imageObject,
    returnImageObject)
from flask_rest_app.api.restplus import api
from flask_rest_app.api.authorization import auth
from flask_rest_app.database.models import Image

from flask_rest_app.api.imageops.imageopspil import (blackAndWhite,
    createSepia, xorSynth, pixelize, line, blur, contrast, mirror, flip,
    swapChannels, greyscale, mask, invert)

log = logging.getLogger(__name__)

ns = api.namespace('imageOps', description='Image operations')

@ns.route('/')
class ImageResources(Resource):
    '''Image resource'''
    @ns.marshal_with(returnImageObject)
    def get(self):
        '''Get all Images'''
        image = Image.query.all()
        print (image)
        return image

    @auth.login_required
    @ns.expect(imageObject)
    @ns.marshal_with(imageObject)
    def post(self):
        '''Insert the image in database'''
        image = createImage(request.json)
        return image, 201

@ns.route('/<int:id>')
class ImageResource(Resource):
    '''Get a specific launcher build'''
    @ns.marshal_with(returnImageObject)
    def get(self, id):
        '''Get specific Image using id'''
        print (id)
        image = Image.query.filter(Image.id == id).one()
        print (image)
        return image

    @auth.login_required
    @ns.response(204, 'Image successfully deleted.')
    def delete(self, id):
        '''Delete the Image using id'''
        deleteImage(id)
        return None, 204

@ns.route('/blackWhite')
class ImageBlackWhiteOp(Resource):
    '''Image Resource'''
    @auth.login_required
    @ns.expect(imageObject)
    @ns.marshal_with(returnImageObject)
    def post(self):
        '''Insert the image and convert to black and white'''
        image = createImage(request.json)
        blackAndWhite(image.imageLocalLocation)
        return image, 201

@ns.route('/Sepia')
class ImageSepiaOp(Resource):
    '''Image Resource'''
    @auth.login_required
    @ns.expect(imageObject)
    @ns.marshal_with(returnImageObject)
    def post(self):
        '''Insert the image and sepia tone it'''
        image = createImage(request.json)
        createSepia(image.imageLocalLocation)
        return image, 201

@ns.route('/Invert')
class ImageInvertOp(Resource):
    '''Image Resource'''
    @auth.login_required
    @ns.expect(imageObject)
    @ns.marshal_with(returnImageObject)
    def post(self):
        '''Insert the image and invert it'''
        image = createImage(request.json)
        invert(image.imageLocalLocation)
        return image, 201

@ns.route('/Mask')
class ImageMaskOp(Resource):
    '''Image Resource'''
    @auth.login_required
    @ns.expect(imageObject)
    @ns.marshal_with(returnImageObject)
    def post(self):
        '''Insert the image and Mask it'''
        image = createImage(request.json)
        mask(image.imageLocalLocation)
        return image, 201

@ns.route('/Grey')
class ImageGreyOp(Resource):
    '''Image Resource'''
    @auth.login_required
    @ns.expect(imageObject)
    @ns.marshal_with(returnImageObject)
    def post(self):
        '''Insert the image and Greyscale'''
        image = createImage(request.json)
        greyscale(image.imageLocalLocation)
        return image, 201

@ns.route('/SwapChannel')
class ImageSwapChannelOp(Resource):
    '''Image Resource'''
    @auth.login_required
    @ns.expect(imageObject)
    @ns.marshal_with(returnImageObject)
    def post(self):
        '''Insert the image and Swap its rgb channels'''
        image = createImage(request.json)
        swapChannels(image.imageLocalLocation)
        return image, 201

@ns.route('/Flip')
class ImageFlipOp(Resource):
    '''Image Resource'''
    @auth.login_required
    @ns.expect(imageObject)
    @ns.marshal_with(returnImageObject)
    def post(self):
        '''Insert the image and flip it'''
        image = createImage(request.json)
        flip(image.imageLocalLocation)
        return image, 201

@ns.route('/Mirror')
class ImageMirrorOp(Resource):
    '''Image Resource'''
    @auth.login_required
    @ns.expect(imageObject)
    @ns.marshal_with(returnImageObject)
    def post(self):
        '''Insert the image and Mirror'''
        image = createImage(request.json)
        mirror(image.imageLocalLocation)
        return image, 201

@ns.route('/Contrast')
class ImageContrastOp(Resource):
    '''Image Resource'''
    @auth.login_required
    @ns.expect(imageObject)
    @ns.marshal_with(returnImageObject)
    def post(self):
        '''Insert the image and contrast it'''
        image = createImage(request.json)
        contrast(image.imageLocalLocation)
        return image, 201

@ns.route('/Blur')
class ImageBlurOp(Resource):
    '''Image Resource'''
    @auth.login_required
    @ns.expect(imageObject)
    @ns.marshal_with(returnImageObject)
    def post(self):
        '''Insert the image and Blur'''
        image = createImage(request.json)
        blur(image.imageLocalLocation)
        return image, 201

@ns.route('/Line')
class ImageLineOp(Resource):
    '''Image Resource'''
    @auth.login_required
    @ns.expect(imageObject)
    @ns.marshal_with(returnImageObject)
    def post(self):
        '''Insert the image and find its fractal lines'''
        image = createImage(request.json)
        line(image.imageLocalLocation)
        return image, 201

@ns.route('/Pixelize')
class ImagePixelizeOp(Resource):
    '''Image Resource'''
    @auth.login_required
    @ns.expect(imageObject)
    @ns.marshal_with(returnImageObject)
    def post(self):
        '''Insert the image and pixelize it'''
        image = createImage(request.json)
        pixelize(image.imageLocalLocation)
        return image, 201

@ns.route('/Xor')
class ImageXorOp(Resource):
    '''Image Resource'''
    @auth.login_required
    @ns.expect(imageObject)
    @ns.marshal_with(returnImageObject)
    def post(self):
        '''Insert the image and do xorSynth over it'''
        image = createImage(request.json)
        xorSynth(image.imageLocalLocation)
        return image, 201
