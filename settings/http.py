import os
import routes
# from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv
from flask import Flask
from model.base import db
from controller import UserController
from controller import Auth
from datetime import timedelta
from flask_jwt import JWT

userController = UserController()
authController = Auth({})
load_dotenv(find_dotenv())



def create_app():
    app = Flask(__name__)
    # accessing variables
    # print( os.getenv('MONGO_URI'))
    app.config['MONGO_URI'] = os.getenv('MONGO_URI')

    app.config['JWT_AUTH_URL_RULE'] = '/api/v1/login'
    # config JWT to expire within half an hour
    # app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)

    # app.config['SECRET_KEY'] = 'super-secret'
    # JWT
    # app.config['JWT_ALGORITHM'] = "HS256"
    app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")
    app.config['JWT_EXPIRATION_DELTA'] = timedelta(days=1)  # token expired in 1 weeks
    #
    #routes mapping
    app.register_blueprint(routes.api.bp)
    app.register_blueprint(routes.user.bp)
    app.debug = True

    # mongoDb initialization
    JWT(app, authController.verify, authController.identity)

    db.init_app(app)

    return app
