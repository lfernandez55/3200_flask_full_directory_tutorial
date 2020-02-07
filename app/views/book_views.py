# Copyright 2014 SolidBuilds.com. All rights reserved
#
# Authors: Ling Thio <ling.thio@gmail.com>


from flask import Blueprint, redirect, render_template

from app import db
#from app.forms.book_forms import BookForm

#after defining the book_blueprint you use it as a decorator in your views below
book_blueprint = Blueprint('books', __name__, template_folder='templates')


@book_blueprint.route('/foo')
def foo():
    return render_template('books/foo.html')

# @book_blueprint.route('/book_form')
# def book_form():
#     book = BookForm()
#     return render_template('books/foo.html')