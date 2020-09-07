import os
import logging

from flask import Flask, jsonify, request
from flask_potion import Api

from config import config_by_name
from application.apis import create_apis
from application.models import db

from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

logger = logging.getLogger()

def create_app(config_name):
    logger.info('Creating app')
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_by_name[config_name])

    logger.info('Configuring database')
    db.init_app(app)
    logger.info('Database configuration finished')

    logger.info('Configuring authetication')
    # Provide a method to create access tokens. The create_access_token()
    # function is used to actually generate the token, and you can return
    # it to the caller however you choose.
    jwt = JWTManager(app)
    @app.route('/api/v1/login', methods=['POST'])
    def login():
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400

        email = request.json.get('email', None)
        password = request.json.get('password', None)

        if not email:
            return jsonify({"msg": "Missing email parameter"}), 400
        if not password:
            return jsonify({"msg": "Missing password parameter"}), 400

        # Identity can be any data that is json serializable
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token), 200
    logger.info('Authentication configuration finished')


    logger.info('Configuring API routes')
    @app.route('/', methods=['GET'])
    def index():
        return 'Welcome to IService'

    api = Api(app, prefix='/api/v1', title='IService')
    create_apis(api)
    logger.info('API routes configuration finished')

    logger.info('App creation finished')

    return app
