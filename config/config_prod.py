import os

from . import Config

class ConfigProd(Config):
    DEBUG = False
    FLASK_ENV = 'production'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{}:{}@{}/{}'.format(
        os.environ['POSTGRES_ISERVICE_PROD_USER'],
        os.environ['POSTGRES_ISERVICE_PROD_PASS'],
        os.environ['POSTGRES_ISERVICE_PROD_SERVER'],
        os.environ['POSTGRES_ISERVICE_PROD_DB'],
    )
