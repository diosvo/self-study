"""
SDK

82 - Create an SDK - Part 1
83 - Create an SDK - Part 2
"""
import importlib
import sqlite3

oop = importlib.import_module('7-oop')


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
    books = []

    for row in cu.execute('SELECT * FROM books'):
        books.append(oop.Book(row[0], row[1]))

    cu.connection.close()

    return books


def get_book_by_title(title: str) -> dict:
    cu = cursor()

    with cu.connection:
        cu.execute('SELECT * FROM books WHERE title=?', (title,))

    return cu.fetchone()


def update_book(book: dict, new_title: str, new_pages: int):
    cu = cursor()

    with cu.connection:
        cu.execute(
            'UPDATE books SET title=?, pages=? WHERE title=? AND pages=?',
            (new_title, new_pages, book.title, book.pages)
        )

    new_book = get_book_by_title(new_title)
    cu.connection.close()

    return new_book


def delete_book(book: dict) -> int:
    cu = cursor()

    with cu.connection:
        cu.execute(
            'DELETE FROM books WHERE title=? AND pages=?',
            (book.title, book.pages)
        )

    rows = cu.rowcount
    cu.connection.close()

    return rows
