"""
api
---
The api package provides Models and routes for creating, viewing, updating and 
deleting blog posts.

"""


import os
import sys

from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_mongoengine import MongoEngine

from api.config import DevelopmentConfig, ProductionConfig, TestingConfig


app = Flask(__name__, static_folder='static', static_url_path='/')
CORS(app)


def set_flask_environment() -> str:
    """Sets the flask development environment

    Loads the environment variable then sets it.

    Raises
    ------
    KeyError
        If the FLASK_ENV environment variable is not set.

    Returns
    -------
    str:
        Flask operating environment i.e test, development or production
    """

    if os.environ['FLASK_ENV'] == 'production':  # pragma: no cover
        app.config.from_object(ProductionConfig)
    elif os.environ['FLASK_ENV'] == 'development':  # pragma: no cover
        app.config.from_object(DevelopmentConfig)
    elif os.environ['FLASK_ENV'] == 'test':
        app.config.from_object(TestingConfig)

    return os.environ['FLASK_ENV']


try:
    flask_env = set_flask_environment()
except KeyError:
    sys.exit("The 'FLASK_ENV' variable is not set.")
db = MongoEngine(app)
ma = Marshmallow(app)

from api import config, models, routes  # isort:skip