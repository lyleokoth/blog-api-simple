"""
Empty module docstring
"""
import os


class BaseConfig():
    """
    Empty class docstring
    """

    SECRET_KEY = os.environ['SECRET_KEY']
    DEBUG = False
    TESTING = False
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class TestingConfig(BaseConfig):
    """Empty class docstring"""

    DEBUG = True
    TESTING = True

    MONGODB_DB = 'flask-react-blog-simple-test'
    MONGODB_HOST = '127.0.0.1'
    MONGODB_PORT = 27017
    MONGODB_USERNAME = ''
    MONGODB_PASSWORD = ''
    MONGODB_CONNECT = True


class DevelopmentConfig(BaseConfig):
    """
    Empty class docstring
    """

    DEBUG = True
    TESTING = False

    MONGODB_DB = 'flask-react-blog-simple-dev'
    MONGODB_HOST = '127.0.0.1'
    MONGODB_PORT = 27017
    MONGODB_USERNAME = ''
    MONGODB_PASSWORD = ''
    MONGODB_CONNECT = True


class ProductionConfig(BaseConfig):
    """
    Empty class docstring
    """

    DEBUG = False
    TESTING = False

    MONGODB_DB = 'flask-react-blog-simple-prod'
    MONGODB_HOST = 'mongodb+srv://cluster0.ctzy7.mongodb.net/'
    MONGODB_PORT = 27017
    MONGODB_USERNAME = 'flask-api'
    MONGODB_PASSWORD = 'flask-api'
    MONGODB_CONNECT = True
