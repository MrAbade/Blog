__version__ = '0.1.1'

from flask import Flask

from config import config_selector
from .configs import config_database


def create_app(config='production'):
    app = Flask(__name__)
    
    app.config.from_object(config_selector[config])

    config_database(app)

    return app
