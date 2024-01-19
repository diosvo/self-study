"""
Any & All Functions
"""

number_to_compare = 30
numbers = [5, 26, 12, 9]
sub_message = f"larger than {number_to_compare}!"


def even(num) -> bool: return num > number_to_compare


result = [even(num) for num in numbers]

if all(result):
    print(f"All numbers are {sub_message}")
elif any(result):
    print(f"At least one number is {sub_message}")
else:
    print(f"No number is {sub_message}")
