# __init__.py is a special Python file that allows a directory to become
# a Python package so it can be accessed using the 'import' statement.

from .book_views import book_blueprint
from .main_views import main_blueprint

def register_blueprints(app):
    app.register_blueprint(book_blueprint)

def register_blueprints(app):
    app.register_blueprint(main_blueprint)