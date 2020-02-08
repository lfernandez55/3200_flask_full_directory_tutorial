from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators

class BookForm(FlaskForm):
    id = StringField('id')
    author = StringField('author')
    title = StringField('title')
    submit = SubmitField()

