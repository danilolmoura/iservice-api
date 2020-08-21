import os

from flask import Flask
from flask_potion import Api

from config import config_by_name
from application.apis import create_apis
from application.models import db

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_by_name[config_name])

    app.logger.info('Connecting database')
    db.init_app(app)

    @app.route('/', methods=['GET'])
    def index():
        return 'Welcome to IService'

    api = Api(app, prefix='/api/v1', title='IService')
    create_apis(api)

    app.logger.info('Finished initialization')

    return app
