import os


class Config(object):
    APP_ROOT = os.path.dirname(os.path.realpath(__file__))
    CONDITIONS_FILE = os.path.join(APP_ROOT, 'conditions.txt')
    DATABASE = os.path.join(APP_ROOT, 'data.db')
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    DATABASE = ':memory:'



