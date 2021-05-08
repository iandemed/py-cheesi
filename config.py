import os

from dotenv import load_dotenv
load_dotenv()


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv("SECRET_KEY")

class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL").replace("://", "ql://", 1) # Enviornment variable saved on Heroku


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    # URI to the local database
    SQLALCHEMY_DATABASE_URI = f'postgresql://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@localhost/cheese'


class TestingConfig(Config):
    TESTING = True