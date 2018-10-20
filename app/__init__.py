from flask import Flask, Blueprint
from flask_jwt_extended import JWTManager


def create_app():
    app = Flask(__name__)

    from instance.config import Config
    app.config.from_object(Config)

    from .api.V1 import productsale_api as psa
    app.register_blueprint(psa)

    app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'

    jwt = JWTManager(app)

    return app
