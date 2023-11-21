"""
Object Oriented Programming (OOP)

What? - It allows to represent everything we want in the code, then we can make the application that exactly needs.
Why? - The foundation for a lot of different things.

65 - Intro to Object Oriented Programming - Classes, __init__, Objects
66 - Creating and Invoking methods
67 - Class level variables
>>> Book.favorites.append(book)

... for item in Book.favorites:
...    print(item)

68 - Intro to method overrides - __str__
69 - __eq__ Method override
>>> book = Book('Are You My Mother?', 72)
... book2 = Book('Are You My Mother?', 72)

70 - __hash__ and Collections
__hash__ = None is the default when we override __eq__ (Book is not hashable)
> Purpose: Quickly compare dictionary keys during a dictionary lookup.
>>> book = Book('Are You My Mother?', 72)
... book2 = Book('Are You My Mother?', 72)

... print(hash(book) == hash(book2))

71 - Passing by Object Reference
"""
print('------------------ Lesson 65 -> 71 ------------------')


class Book():
    favorites = []

    def __init__(self, title: str, pages: int) -> None:
        self.title = title
        self.pages = pages

    def is_long(self):
        return True if self.pages > 100 else False

    def __str__(self) -> str:
        return f"'{self.title}' is {self.pages} pages long"

    def __eq__(self, other: object) -> bool:
        return self.title == other.title and self.pages == other.pages

    def __hash__(self) -> int:
        return hash(self.title) ^ hash(self.pages)

    def __repr__(self) -> str:  # added to make list of items invoke str
        return self.__str__()


"""
FILE PROCESSING

72 - File IO - Reading and Writing to .txt file
73 - Intro to Exception handling
74 - Exception handling using `with`
"""
print('------------------ Lesson 72 -> 74 ------------------')

try:
    file = open('/tmp/input.txt', 'r')

except FileNotFoundError as e:
    print(e)

except OSError as e:
    print(e)

except Exception as e:
    print(e)

else:
    with file:
        print(file.readline() or 'Empty file.')

finally:
    file.close()
    print('finished!')
