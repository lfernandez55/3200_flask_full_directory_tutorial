# Copyright 2014 SolidBuilds.com. All rights reserved
#
# Authors: Ling Thio <ling.thio@gmail.com>


from flask import Blueprint, render_template

from app import db
from app.models.book_models import Book

#after defining the main_blueprint you use it as a decorator in your views below
main_blueprint = Blueprint('main', __name__, template_folder='templates')

@main_blueprint.route('/')
def home():
    return render_template('main/index.html')

@main_blueprint.route('/db_view')
def db_view():
    db.create_all()
    book = Book(author="Dr. Seuss", title="The Cat in the Hat")
    db.session.add(book)
    db.session.commit()
    book_from_db = Book.query.filter(Book.id == 1).first()
    return_string = "DB methods executed!!! Record added: " + book_from_db.author + " " + book_from_db.title
    return(return_string)