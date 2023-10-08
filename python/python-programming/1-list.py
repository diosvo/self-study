"""
2 - Intro to Lists

Method - a function is attached to an object.
Function - a sequence of statement.
"""
print('------------------ Lesson 2 ------------------')

fruits = ['apple', 'banana']

fruits.append('pineapple')  # method
length = len(fruits)  # function

print('length:', length)

"""
3 - Check if Item in List
"""
print('------------------ Lesson 3 ------------------')

if 'pineapple' not in fruits:
    print('Buy it...')
else:
    print('Eating the pineapple')

"""
4 - Working with Lists
"""
print('------------------ Lesson 4 ------------------')

backpack = ['pineapple', 'pizza', 'steak', 'chips']

if 'pizza' not in fruits:
    backpack.remove('pizza')
    print(backpack)

"""
5 - Removing from Lists using List Comprehension
6 - Intro to List Comprehension

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
7 - Length of List with len
"""
print('------------------ Lesson 7 ------------------')

for i in range(len(fruits)):
    print(i, fruits[i])

"""
8 - Count - Counting an Element in List
"""
print('------------------ Lesson 8 ------------------')

print(fruits.count('banana'))
