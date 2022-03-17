from distutils.debug import DEBUG
import os


class Config:
    SECRET_KEY = '1234'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaaccess:bloghhh@localhost/bloghhh'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI =  os.environ.get("SQLALCHEMY_DATABASE_URI")
    


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
