"""
1. Standard library import
2. Third party library import
3. local packages import
"""
from flask import Flask
from flask_restful import Api
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
from config import ConfigClass
from errors import errors

# api = Api(errors=errors)
db = MongoEngine()
mail = Mail()
jwt = JWTManager()
crypto = Bcrypt()


def create_app(config_class=ConfigClass):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from resources.routes import api
    api.init_app(app)
    mail.init_app(app)
    jwt.init_app(app)
    crypto.init_app(app)
    db.init_app(app)

    # from resources.routes import initialize_routes
    # initialize_routes(api)

    return app
