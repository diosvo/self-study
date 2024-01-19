"""
Map Function
"""

numbers = [14, 23, 8, 12, 2, 5, 26]


def square(num: int) -> int:
    return num * num


transformer = map(square, numbers)

mapped_fn = list(transformer)
