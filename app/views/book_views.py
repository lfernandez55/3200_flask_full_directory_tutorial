# Copyright 2014 SolidBuilds.com. All rights reserved
#
# Authors: Ling Thio <ling.thio@gmail.com>


from flask import Blueprint, redirect, render_template
from flask import request, url_for


#from app import db

book_blueprint = Blueprint('books', __name__, template_folder='templates')


@book_blueprint.route('/foo')
def foo():
    return render_template('books/foo.html')
