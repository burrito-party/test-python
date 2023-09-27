
from flask import request, render_template, make_response

from server.webapp import flaskapp, cursor
from server.models import Book


@flaskapp.route('/')
def index():
    name = request.args.get('name')
    author = request.args.get('author')
    read = bool(request.args.get('read'))

    if name:
        sql = "SELECT * FROM books WHERE name LIKE %s"
        cursor.execute(sql, ('%' + name + '%',))

    elif author:
        sql = "SELECT * FROM books WHERE author LIKE %s"
        cursor.execute(sql, ('%' + author + '%',))

    else:
        cursor.execute("SELECT name, author, read FROM books")

    books = [Book(*row) for row in cursor]

    return render_template('books.html', books=books)
