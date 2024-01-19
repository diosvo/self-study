"""
Swapping Variables
"""

first = 24
second = 41

"""
Manual way

>>> temp = first
... first = second
... second = temp
"""

# Best Approach

first, second = second, first
