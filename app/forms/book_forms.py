from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators

class BookForm(FlaskForm):
    id = IntegerField('id')
    book_name = StringField('book_name')