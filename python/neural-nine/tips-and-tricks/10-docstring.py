"""
Docstring
"""


def calculation(num_1: int | float, num_2: int | float) -> int | float:
    """
    The functions takes one number to the power of another number and returns the result.

    :param num_1: The base
    :param num_2: The exponent
    :return: The result of the calculation
    """
    return num_1 ** num_2


print(calculation(10, 2))
