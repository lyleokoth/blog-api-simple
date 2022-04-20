"""
Empty module docstring
"""
import os

from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_mongoengine import MongoEngine

from api.config import DevelopmentConfig, ProductionConfig, TestingConfig

app = Flask(__name__, static_folder='static', static_url_path='/')
CORS(app)


def set_flask_environment() -> str:
    """Sets the flask development environment

    Raises
    ------
    KeyError

    Returns
    -------
    str:
        Flask operating environment i.e development or production
    """

    if os.environ['FLASK_ENV'] == 'production':  # pragma: no cover
        app.config.from_object(ProductionConfig)
    elif os.environ['FLASK_ENV'] == 'development':  # pragma: no cover
        app.config.from_object(DevelopmentConfig)
    elif os.environ['FLASK_ENV'] == 'test':
        app.config.from_object(TestingConfig)

    return os.environ['FLASK_ENV']


flask_env = set_flask_environment()
db = MongoEngine(app)
ma = Marshmallow(app)

from api import config, models, routes  # isort:skip