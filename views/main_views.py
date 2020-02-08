# Copyright 2014 SolidBuilds.com. All rights reserved
#
# Authors: Ling Thio <ling.thio@gmail.com>


from flask import Blueprint, render_template

from app import db
from models.book_models import Book
from forms.book_forms import BookForm

# after defining the main_blueprint you use it as a decorator in your views below
main_blueprint = Blueprint('main', __name__, template_folder='templates')

@main_blueprint.route('/')
def home():
    return render_template('main/index.html')

