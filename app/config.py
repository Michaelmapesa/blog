
import os

class Config:
    SECRET_KEY = '12345'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaaccess:mapesa@localhost/mapesa'
    DEBUG = True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = False


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
}