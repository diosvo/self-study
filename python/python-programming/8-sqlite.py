"""
SQLite & DATABASE

76 - Intro to SQLite and Creating a Database
77 - Create a SQLite Table in SQLite
78 - Insert data to Database
79 - Retrieve Database data
80 - Delete Database data
81 - Update SQLite data
"""
import sqlite3

print('------------------ Lesson 76 -> 81 ------------------')

conn = sqlite3.connect(':memory:')  # connect to a database in RAM

# Once a connection has been established, create a Cursor object and call
# its execute() or executemany() method to perform SQL queries:
cu = conn.cursor()

# 77
cu.execute('CREATE TABLE IF NOT EXISTS books (title TEXT, pages INTEGER)')

# 78
cu.execute("INSERT INTO books (title) VALUES ('Are you my mother')")
cu.execute("INSERT INTO books VALUES ('Homo Sapiens', 500)")

books = [
    ('The giving tree', 66),
    ('The digging-est dog', 77)
]
cu.executemany('INSERT INTO  books VALUES (?, ?)', books)
conn.commit()

# 80
cu.execute("DELETE FROM books WHERE title='Are you my mother'")
conn.commit()

# 81
cu.execute("UPDATE books SET title='New Book' WHERE rowid=3")
conn.commit()

# 79
cu.execute('SELECT rowid, title FROM books')
data = cu.fetchall()

print('Fetch all data after deletion:', data)

"""
SDK

82 - Create SDK - Part 1
82 - Create SDK - Part 2
"""
print('------------------ Lesson 82 -> 83 ------------------')

# Python modules
import importlib
from os.path import dirname
import sys

# Expand system path
sys.path.append(dirname(__file__) + '/modules/')

# Development modules
import sdk
oop = importlib.import_module('7-oop')

book = oop.Book('Hitler', 1000)

# sdk.add_book(book)
# sdk.get_books()
print(sdk.get_book_by_title('Hitler'))
