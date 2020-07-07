from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # don't forget to change this before deploying.
    app.config['SECRET_KEY'] = 'dev'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite3'

    db.init_app(app)

    from .views import pages
    app.register_blueprint(pages)

    return app

# generating the database using SQLAlchemy.

# from unolibrary import db, create_app
# from .models import Books, Authors

# db.create_all(app=create_app())