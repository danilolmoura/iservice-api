import os

from . import Config

class ConfigTest(Config):
    DEBUG = True
    TESTING = True
    FLASK_ENV = 'testing'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{}:{}@{}/{}'.format(
        os.environ['POSTGRES_ISERVICE_TEST_USER'],
        os.environ['POSTGRES_ISERVICE_TEST_PASS'],
        os.environ['POSTGRES_ISERVICE_TEST_SERVER'],
        os.environ['POSTGRES_ISERVICE_TEST_DB'],
    )