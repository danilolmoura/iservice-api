import os

from . import Config

class ConfigTest(Config):
    DEVELOPMENT = True
    DEBUG = True
    TESTING = True
    FLASK_ENV = 'test'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{}:{}@{}/{}'.format(
        os.environ['POSTGRES_USER_TEST'],
        os.environ['POSTGRES_PASSWORD_TEST'],
        os.environ['POSTGRES_SERVER_TEST'],
        os.environ['POSTGRES_DB_TEST'],
    )
