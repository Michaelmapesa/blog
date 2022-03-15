import os


class Config:
    SECRET_KEY = '12345'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaaccess:mapesa@localhost/mapesa'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaaccess:mapesa@localhost/mapesa'


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}