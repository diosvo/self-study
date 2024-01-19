"""
Amount of Digits in A Number
"""

import math

number = 99999999999999999999997

# Manual way

digit_amount = len(str(number))

# Logarithmic Function

if number > 0:
    logarithmic_amount = math.ceil(math.log10(number)) + 1
elif number < 0:
    logarithmic_amount = math.ceil(math.log10(-number)) + 1
else:
    logarithmic_amount = 1

# Best Approach

counter = 1

while abs(number) >= (10 ** counter):
    counter += 1
