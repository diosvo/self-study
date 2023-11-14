from collections import Counter

"""
10 - Count Each Element in List - List Comprehension
"""
print('------------------ Lesson 10 ------------------')

animals = ['dog', 'cat', 'bird', 'horse', 'horse', 'cat']

[print(animals.count(item), item) for item in set(animals)]

"""
11 - Counter (from collections)
12 - Basic Collections Review
"""
print('------------------ Lesson 11 -> 12 ------------------')

print(Counter(animals))

"""
DICTIONARIES w/ Set operations

60 - Working with Sets
"""
print('------------------ Lesson 60 ------------------')

conjunctions = {'for', 'to', 'so', 'by'}
seen = set()

original_poem = """
I still feel your touch in my dreams
Forgive me my weakness, but I don't know why
Without you it's hard to survive
'Cause every time we touch, I get this feeling
And every time we kiss I swear I could fly
Can't you feel my heart beat fast, I want this to last
Need you by my side"""

data = original_poem.split()

for word in data:
    if str.lower(word) in conjunctions:
        seen.add(str.lower(word))

print(seen)

"""
61 - Remove duplicates in a List using Sets
"""
print('------------------ Lesson 61 ------------------')

colors = ['red', 'red', 'blue', 'blue', 'green', 'blue']

count = [[colors.count(key), key] for key in set(colors)]

print(count)

"""
62 - Union and Intersection
63 - Difference and Symmetric Difference

# Union
>>> my_fav | her_fav

# Intersection
>>> my_fav & her_fav

63 - Difference and Symmetric Difference

# Difference
>>> my_fav - her_fav

# Symmetric Difference
>>> my_fav ^ her_fav
"""
print('------------------ Lesson 62 -> 63 ------------------')

my_fav = {'red', 'green', 'blue', 'black', 'purple'}
her_fav = {'blue', 'purple', 'green'}

print(my_fav ^ her_fav)