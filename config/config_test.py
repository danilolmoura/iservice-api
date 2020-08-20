import os

from . import Config

class ConfigTest(Config):
    DEVELOPMENT = True
    DEBUG = True
    TESTING = True
    FLASK_ENV = 'testing'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{}:{}@{}/{}'.format(
        os.environ['POSTGRES_USER_TEST_ISERVICE'],
        os.environ['POSTGRES_PASSWORD_TEST_ISERVICE'],
        os.environ['POSTGRES_SERVER_TEST_ISERVICE'],
        os.environ['POSTGRES_DB_TEST_ISERVICE'],
    )
