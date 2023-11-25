"""
87 - Intro to Tkinter GUI Development
88 - Complete Guessing Game in Tkinter
"""

import tkinter
from tkinter import messagebox
from random import randint

low = 0
high = 20
rand = randint(low, high)
print(rand)


def check(guess: int):
    if guess < rand:
        messagebox.showwarning('Oops!', f'{guess} is too low.')
    elif guess > rand:
        messagebox.showwarning('Oops!', f'{guess} is too high.')
    else:
        tkinter.messagebox.showinfo('Win!', f'{guess} is correct.')


tk = tkinter.Tk()
tk.title('Guessing Game')

label = tkinter.Label(tk, text=f'Guess a number {low} to {high} (inclusive)')
label.pack()

entry = tkinter.Entry(tk)
entry.pack()

button = tkinter.Button(
    tk, text='Guess', command=lambda: check(int(entry.get()))
)
button.pack()

tk.mainloop()
