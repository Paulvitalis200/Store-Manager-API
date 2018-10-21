from flask import Flask, Blueprint


def create_app():
    app = Flask(__name__)

    from instance.config import Config
    app.config.from_object(Config)

    from .api.V1 import productsale_api as psa
    app.register_blueprint(psa)

    return app
