import os

from . import Config

class ConfigDev(Config):
    DEBUG = True
    FLASK_ENV = 'development'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{}:{}@{}/{}'.format(
        os.environ['POSTGRES_ISERVICE_DEV_USER'],
        os.environ['POSTGRES_ISERVICE_DEV_PASS'],
        os.environ['POSTGRES_ISERVICE_DEV_SERVER'],
        os.environ['POSTGRES_ISERVICE_DEV_DB'],
    )
