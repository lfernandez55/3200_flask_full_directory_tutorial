from app import db

class Book(db.Model):
    __tablename__ = 'Book'
    id = db.Column(db.Integer(), primary_key=True)
    author = db.Column(db.String(50), nullable=False, server_default=u'', unique=False)
    title = db.Column(db.String(100), nullable=False, server_default=u'', unique=False)


