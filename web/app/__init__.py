from flask import Flask
from config import config


def create_app(config: config):
    app = Flask(__name__)

    from app import routes
    routes.load(app)

    return app
