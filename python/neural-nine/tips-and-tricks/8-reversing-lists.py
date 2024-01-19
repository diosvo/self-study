"""
Reversing Lists
"""
values = [1, 2, 3, 4, 5]

# Manual way

rev_list = []
for index in range(len(values)):
    rev_list.append(values[len(values) - index - 1])

# Reverse Methods

"""
1. Change the original list.

>>> values.reverse()
"""

"""
2. Do NOT apply to the actual list.
-> Need to assign to a variable.

>>> values = list(reversed(values))
"""

"""
3. Use index slice
"""
values = values[::-1]
