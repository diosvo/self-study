"""
Zip Function
"""

names = ["Dios", "Kitu"]
ages = [25, 27]

# Manual way

for index in range(len(names)):
    list = f"{names[index]} - {ages[index]}"

# Zip Function

for name, age in zip(names, ages):
    list = f"{name} - {age}"

"""
Practical Examples
"""

# 1. Calculate Profit

sales = [500, 800, 300]
costs = [200, 199, 222]

for sale, cost in zip(sales, costs):
    profit = sale - cost

# 2. Separate into tuple list

zipped = [("Dios", 25), ("Kitu", 27)]

names, ages = zip(*zipped)

# 3. Map to the dictionary

letters = ["b", "d", "a", "c"]
numbers = [3, 2, 4, 1]

data = dict(zip(letters, numbers))
