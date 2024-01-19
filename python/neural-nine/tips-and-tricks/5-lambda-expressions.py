"""
Lambda Expressions
"""
from typing import Callable

# Multiple Parameters

square_fn = lambda *args: sum(args)

"""
Practical Examples
"""

numbers = [0, 5, 26, 12, 9, 100, 7]

squared_numbers = list(map(lambda num: num ** 2, numbers))

print(squared_numbers)

# Lambda Expressions in Functions


def custom_fn(num: int) -> Callable[..., int]:
    return lambda item: item * num


multiple = custom_fn(10)
