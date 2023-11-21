"""
SDK

82 - Create an SDK - Part 1
83 - Create an SDK - Part 2
"""
import sqlite3


def cursor() -> sqlite3.Cursor:
    return sqlite3.connect('/tmp/books.db').cursor()


cu = cursor()
cu.execute('CREATE TABLE IF NOT EXISTS books (title TEXT, pages INTEGER)')
cu.connection.close()


def add_book(book: dict) -> int | None:
    cu = cursor()

    with cu.connection:
        cu.execute('INSERT INTO books VALUES (?, ?)', (book.title, book.pages))

    return cu.lastrowid


def get_books():
    cu = cursor()

    with cu.connection:
        cu.execute('SELECT * FROM books')

    return cu.fetchall()


def get_book_by_title(title: str) -> dict:
    cu = cursor()

    with cu.connection:
        cu.execute('SELECT * FROM books WHERE title=?', (title,))

    return cu.fetchone()
