from secrets import token_hex
from os import getenv


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = token_hex(32)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://mrabade:pain321123@localhost/Blog'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URL')


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'


config_selector = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'test': TestConfig
}
