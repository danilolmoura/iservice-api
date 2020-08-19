import os

from . import Config

class ConfigDev(Config):
    DEVELOPMENT = True
    DEBUG = True
    FLASK_ENV = 'dev'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{}:{}@{}/{}'.format(
        os.environ['POSTGRES_USER_DEV'],
        os.environ['POSTGRES_PASSWORD_DEV'],
        os.environ['POSTGRES_SERVER_DEV'],
        os.environ['POSTGRES_DB_DEV'],
    )
