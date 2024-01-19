"""
Merging Dictionaries
"""

first = {"a": 1, "b": "2"}
second = {"c": 1, "d": "2"}

# Update Method

"""
1. Use `update` function

>>> first.update(second)
... print(first)
"""

"""
2. Use keyword argument operator (**)

>>> merged = {**first, **second}
... print(merged)
"""

# Modern Method

"""
1. Python 3.9+

>>> merged = first | second
... print(merged)
"""

"""
2. All
"""
merged = dict(first.items() | second.items())
