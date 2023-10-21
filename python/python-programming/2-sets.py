from collections import Counter

"""
10 - Count Each Element in List - List Comprehension
"""
print('------------------ Lesson 10 ------------------')

animals = ['dog', 'cat', 'bird', 'horse', 'horse', 'cat']

[print(animals.count(item), item) for item in set(animals)]

"""
11 - Counter (from collections)
"""
print('------------------ Lesson 11 ------------------')

print(Counter(animals))

"""
12 - Basic Collections Review
"""
print('------------------ Lesson 12 ------------------')