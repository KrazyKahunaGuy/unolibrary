from . import db

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(256), nullable=False)
    author_name = db.Column(db.String(256), nullable=False)
    summary = db.Column(db.String(4096))

class Authors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_name =db.Column(db.String(256), nullable=False)
    bio = db.Column(db.String(4096))