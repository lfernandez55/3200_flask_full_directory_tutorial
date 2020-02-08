from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# the db is defined globally - so a little differently than how we used to do it
# see how it's connected to the flask app below
db = SQLAlchemy()

# Initialize Flask Application
def create_app(extra_config_settings={}):

    # Instantiate Flask
    app = Flask(__name__)

    # # Load settings
    app.config.from_pyfile('settings.py')

    # Setup Flask-SQLAlchemy
    # up to now we did: db = SQLAlchemy(app) now we do:
    db.init_app(app)

    # Register blueprints
    from views import register_blueprints
    register_blueprints(app)

    return app

# Start development web server
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=7000, debug=True)
