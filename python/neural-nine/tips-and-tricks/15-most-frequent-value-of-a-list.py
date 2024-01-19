"""
Most Frequent Value of A List
"""

from collections import Counter

numbers = [1, 2, 3, 4, 1, 2, 1, 1, 3, 2, 4, 1, 3, 2, 4, 2, 3, 2, 3, 1, 2, 4]

# Dump Method

current_max = 0
current_value = None

for num in numbers:
    if numbers.count(num) > current_max:
        current_max = numbers.count(num)
        current_value = num

# Counter Method

counter = Counter(numbers)
most_common = counter.most_common(1)

# Max Method - Best Approach

most_frequent = max(set(numbers), key=numbers.count)
frequency = numbers.count(most_frequent)
