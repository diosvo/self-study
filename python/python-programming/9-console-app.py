"""
84 - Creating a Library Console App
85 - Updating and Deleting books through console app
"""
import importlib
import sys
from os.path import dirname

# Expand system path
sys.path.append(dirname(__file__) + '/modules/')

# Development modules
import sdk
oop = importlib.import_module('7-oop')


def print_menu():
    print("""Choose an option:
        1. Get all books
        2. Add a new book
        3. Update a book
        4. Delete a book
    """)


while True:
    print_menu()
    response = int(input())

    if response == 1:
        [print(book) for book in sdk.get_books()]
    elif response == 2:
        print('What is the name of the book?')
        title = input()
        print('How many pages is the book?')
        pages = int(input())

        book = oop.Book(title, pages)

        sdk.add_book(book)
    elif response == 3:
        print('What is the current title?')
        title = input()
        print('Current number of pages?')
        pages = int(input())

        book = oop.Book(title, pages)

        print('What is the new title?')
        new_title = input()
        print('New number of pages?')
        new_pages = int(input())

        sdk.update_book(book, new_title, new_pages)
    elif response == 4:
        print('What is the title?')
        title = input()
        print('Number of pages?')
        pages = int(input())

        book = oop.Book(title, pages)

        sdk.delete_book(book)
    else:
        print('Thanks for using our sweet app!')
        break
