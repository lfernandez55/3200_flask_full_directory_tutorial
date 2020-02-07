# __init__.py is a special Python file that allows a directory to become
# a Python package so it can be accessed using the 'import' statement.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# the db is defined globally - so a little differently than how we used to do it
# see how it's connected to the flask app below
db = SQLAlchemy()

# Initialize Flask Application
def create_app(extra_config_settings={}):

    # Instantiate Flask
    app = Flask(__name__)

    # Load common settings
    app.config.from_object('app.settings')
    # Load extra settings from extra_config_settings param
    app.config.update(extra_config_settings)

    # Setup Flask-SQLAlchemy
    # up to now we did: db = SQLAlchemy(app) now we do:
    db.init_app(app)

    # Register blueprints
    from .views import register_blueprints
    register_blueprints(app)


    return app


