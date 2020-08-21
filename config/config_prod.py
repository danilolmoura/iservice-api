import os

from . import Config

class ConfigProd(Config):
    DEBUG = False
    FLASK_ENV = 'production'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{}:{}@{}/{}'.format(
        os.environ['POSTGRES_USER_PROD_ISERVICE'],
        os.environ['POSTGRES_PASSWORD_PROD_ISERVICE'],
        os.environ['POSTGRES_SERVER_PROD_ISERVICE'],
        os.environ['POSTGRES_DB_PROD_ISERVICE'],
    )
