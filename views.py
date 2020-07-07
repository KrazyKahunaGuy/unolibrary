from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import Books, Authors

pages = Blueprint('pages', __name__)

@pages.route('/')
def home():
    return render_template('home.html')

@pages.route('/books')
def books():
    books = Books.query.all()
    return render_template('all_books.html', books=books)

@pages.route('/authors')
def authors():
    authors = Authors.query.all()
    return render_template('all_authors.html', authors=authors)

@pages.route('/new_book')
def new_book():
    return render_template('new_book.html')

@pages.route('/new_book', methods=['POST'])
def new_book_post():
    book_title = request.form.get('book-title')
    author_name = request.form.get('author-name')
    summary = request.form.get('summary')
    
    new_book = Books(book_title = book_title, author_name = author_name, summary = summary)
    db.session.add(new_book)
    db.session.commit()

    return redirect(url_for('pages.new_book'))

@pages.route('/new_author')
def new_author():
    return render_template('new_author.html')

@pages.route('/new_author', methods=['POST'])
def new_author_post():
    author_name = request.form.get('author-name')
    bio = request.form.get('bio')
    
    new_author = Authors(author_name = author_name, bio = bio)
    db.session.add(new_author)
    db.session.commit()

    return redirect(url_for('pages.new_author'))