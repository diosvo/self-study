"""
[2] - Intro to Lists

Method - a function is attached to an object.
Function - a sequence of statement.
"""
print('------------------ Lesson 2 ------------------')

fruits = ['apple', 'banana']

fruits.append('pineapple')  # method
length = len(fruits)  # function

print('length:', length)

"""
[3] - Check if item in List
"""
print('------------------ Lesson 3 ------------------')

if 'pineapple' not in fruits:
    print('Buy it...')
else:
    print('Eating the pineapple')

"""
[4] - Working with Lists
"""
print('------------------ Lesson 4 ------------------')

backpack = ['pineapple', 'pizza', 'steak', 'chips', 'apple', 'pineapple']

if 'pizza' not in fruits:
    backpack.remove('pizza')
    print(backpack)

"""
[5] - Removing from Lists using List Comprehension
[6] - Intro to List Comprehension

[:] - without actually creating a new list,
it means the original list is modified.
"""
print('------------------ Lesson 5 -> 6 ------------------')

# print('before:', id(backpack))
backpack[:] = [item for item in backpack if item in fruits]

print(backpack)
# print('after:', id(backpack))

squares = [i ** 2 for i in range(10) if i % 2 == 0]
print(squares)

"""
[7] - Length of List with `len`
"""
print('------------------ Lesson 7 ------------------')

for i in range(len(fruits)):
    print(i, fruits[i])

"""
[8] - Count - Counting an Element in List
"""
print('------------------ Lesson 8 ------------------')

print(fruits.count('banana'))

"""
[13] - Insert into List
"""
print('------------------ Lesson 13 ------------------')

workdays = ['Monday', 'Tuesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

workdays.insert(2, 'Wednesday')

print(workdays)

"""
BASIC REMOVAL

Basic way:
>>> workdays.remove('Saturday')

[14] - Remove item by index from List with `del`
>>> del workdays[-1]

[15] - Remove item from List with `pop`
"""
print('------------------ Lesson 14 -> 15 ------------------')

workdays.pop(5)

print(workdays)

"""
SLICING

[16] - Slicing with `del` operator

[17] - Removing all occurrences of item in List
>>> while backpack.count('pineapple') > 0:
>>>     backpack.remove('pineapple')

Remove all occurrences of item using `while` is not good idea.

[18] - Slicing a list and [:] explained (same as lesson 6)
>>> second_backpack = backpack[:]

Not a same object in memory, they are going to be pretty much copy of each other
They just happen to be exactly the same in terms of contents.
"""
print('------------------ Lesson 16 -> 18 ------------------')

del workdays[workdays.index('Wednesday'):]

print(workdays)

"""
ADVANCED REMOVAL

[19] - Remove elements from List with `for` loop
>>> new_backpack = []
... for item in backpack[:]:
...    if item != 'pineapple':
...       new_backpack.append(item)
... backpack = new_backpack

[20] - Remove elements using List Comprehension
"""
print('------------------ Lesson 19 -> 20 ------------------')

backpack[:] = [item for item in backpack if item != 'pineapple']

print(backpack)

"""
REVERSE

[21] - How to use `reverse` method with Lists
>>> data.reverse()

[22] - How to swap variables and list elements
>>> me = 'dios'
... you = 'wade'
... me, you = you, me

[23] - Reverse list Algorithm (O(n))
>>> for index in range(len(data) // 2):
...    data[index], data[-index-1] = data[-index-1], data[index]

[24] - Reverse Iterator
>>> data_reversed = []
... for item in reversed(data):
...    data_reversed.append(item)

🌟 [25] - Reverse List with slice

[::<step>] - the amount you want to go each time,
or what direction you want to go
"""
print('------------------ Lesson 21 -> 25 ------------------')

data = [0, 1, 2, 3, 4, 5, 6]

data[:] = data[::-1]
data.reverse()

print(data)

"""
SORTING

[27] - Sort List with `sort` method
>>> workdays.sort()

[28] - Sort with the `sorted` method
>>> sorted(workdays)

It creates new data set, so `sort` method is preferred

[29] - Sort data in reverse order

>>> data.sort()
... data.reverse()
or
>>> sorted(data, reverse=True)

---

>>> strings = [ 'a','A','abc','ABC', 'AAA', 'aBC', 'HELLO']

[30] - Case insensitive sort
>>> strings.sort(key=str.lower)

[31] - Sort by string length
>>> strings.sort(key=len)
or
>>> sorted(strings, key=len)

[32] - Lexicographic number sort (sort number as strings)
>>> numbers.sort(key=str)

[33] - Compare and sort various types
"""
print('------------------ Lesson 27 -> 34 ------------------')

age = 5
stuff = [True, False, 0, -1, "0", "10", age < 30, "2", "9011", "5.5", "6.0", 6]

stuff.sort(key=float)

print(stuff)