from setuptools import setup, find_packages

setup(
    name='flask_rest_app',
    version='1.0.0',
    description='rest api services for putting load',

    keywords='rest restful api flask swagger openapi flask-restplus',

    packages=find_packages(),

    install_requires=['flask-restplus==0.9.2', 'Flask-SQLAlchemy==2.1'],
)
