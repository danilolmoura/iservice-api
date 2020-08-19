import os

from . import Config

class ConfigProd(Config):
    DEVELOPMENT = False
    DEBUG = False
    FLASK_ENV = 'prod'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{}:{}@{}/{}'.format(
        os.environ['POSTGRES_USER_PROD'],
        os.environ['POSTGRES_PASSWORD_PROD'],
        os.environ['POSTGRES_SERVER_PROD'],
        os.environ['POSTGRES_DB_PROD'],
    )
