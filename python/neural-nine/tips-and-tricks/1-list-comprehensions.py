"""
List Comprehensive
"""

numbers = [1, 3, 99, 26, 12, 5]

# Number interaction

list = [item for item in numbers if item % 2 == 0]

powers_of_two = [2 ** item for item in numbers]

# String interaction with Else branches

words = ["automobile", "car", "anger", "fox", "anchor"]

transform_words = [
    word.upper() if word.startswith('a') else word
    for word in words
]
