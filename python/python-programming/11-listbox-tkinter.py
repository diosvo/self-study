"""
89 - Tkinter Listbox - Display a List of Data
90 - Button to Add / Remove Tkinter Listbox Items
91 - Working with SQLite in Tkinter - Adding books
92 - Working with SQLite in Tkinter - Removing books
"""
import importlib
import sys
import tkinter
from tkinter import END
from os.path import dirname

# Expand system path
sys.path.append(dirname(__file__) + '/modules/')

# Development modules
import sdk
oop = importlib.import_module('7-oop')

books = []
tk = tkinter.Tk()
tk.title('Listbox')

def add_to_list():
    if title.get() == '' or pages.get() == '':
        return

    book = oop.Book(title_entry.get(), int(pages_entry.get()))

    if (sdk.add_book(book)):
        books.append(book)
        listbox.insert(END, book)

    title_entry.delete(0, END)
    pages_entry.delete(0, END)


def remove_from_list():
    book_tuple = listbox.curselection()
    book = books.pop(book_tuple[0])

    if (sdk.delete_book(book)):
        listbox.delete((book_tuple))

listbox = tkinter.Listbox(tk)


for book in sdk.get_books():
    books.append(book)
    listbox.insert(END, book)

listbox.pack()

title = tkinter.Label(tk, text='Book title:')
title.pack()

title_entry = tkinter.Entry(tk)
title_entry.pack()

pages = tkinter.Label(tk, text='Book pages:')
pages.pack()

pages_entry = tkinter.Entry(tk)
pages_entry.pack()

add_btn = tkinter.Button(tk, text='Add book', command=add_to_list)
add_btn.pack()

remove_btn = tkinter.Button(tk, text='Remove book', command=remove_from_list)
remove_btn.pack()

tk.mainloop()
