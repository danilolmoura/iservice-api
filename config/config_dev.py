import os

from . import Config

class ConfigDev(Config):
    DEBUG = True
    FLASK_ENV = 'development'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{}:{}@{}/{}'.format(
        os.environ['POSTGRES_USER_DEV_ISERVICE'],
        os.environ['POSTGRES_PASSWORD_DEV_ISERVICE'],
        os.environ['POSTGRES_SERVER_DEV_ISERVICE'],
        os.environ['POSTGRES_DB_DEV_ISERVICE'],
    )
