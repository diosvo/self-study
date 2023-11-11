"""
DICTIONARIES

data = {
    'caleb': 'caleb@gmail.com',
    'tim': 'tim@gmail.com',
}

55 - Intro to dictionaries
56 - Properly retrieve data from dictionary
>>> data.get('email', 'No email found')

57 - Add items to dictionary (3 ways)
>>> data['new_key'] = new_value
or
>>> data.update({'new_key': new_value})
or
>>> data.update(new_key=new_value)

58 - Loop through dictionary
>>> for key in data:
...   print(key, data[key])

59 - Looping through Key Value airs + Counting words
"""
print('------------------ Lesson 55 -> 59 ------------------')

conjunctions = {
    'for': 0,
    'to': 0,
    'so': 0,
    'by': 0
}

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
        conjunctions[str.lower(word)] += 1

print(conjunctions)
