# Copyright 2014 SolidBuilds.com. All rights reserved
#
# Authors: Ling Thio <ling.thio@gmail.com>


from flask import Blueprint, redirect, render_template

from app import db
from models.book_models import Book
from forms.book_forms import BookForm

#after defining the book_blueprint you use it as a decorator in your views below
book_blueprint = Blueprint('books', __name__, template_folder='templates')

@book_blueprint.route('/foo')
def foo():
    return render_template('books/foo.html')

@book_blueprint.route('/db_view')
def db_view():
    db.create_all()
    book = Book(author="Dr. Seuss", title="The Cat in the Hat")
    db.session.add(book)
    db.session.commit()
    book_from_db = Book.query.filter(Book.id == 1).first()
    return_string = "DB methods executed!!! Record added: " + book_from_db.author + " " + book_from_db.title
    return(return_string)

@book_blueprint.route('/book_form')
def book_form():
    form = BookForm()
    print(form)
    return render_template('books/new_book.html', form=form)