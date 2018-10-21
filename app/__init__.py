from flask import Flask


def create_app():
    app = Flask(__name__)

    from instance.config import Config
    app.config.from_object(Config)

    return app
