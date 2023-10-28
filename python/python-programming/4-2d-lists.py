from typing import List

"""
List of Lists (2D Lists)

42 - Working with List of Lists (2D Lists)
43 - Create function to print 2D List
"""
print('------------------ Lesson 42 -> 43 ------------------')

data = [[9, 26], [12, 9], [5, 500, 11]]


def print_2d(data: List[list]) -> None:
    for inner_list in data:
        for grade in inner_list:
            print(grade, end=" ")
        print()


print_2d(data)

"""
44 - Combining List elements with `join` method
"""
print('------------------ Lesson 44 ------------------')

message = ['this', 'is', 'data', 5, 10]

print(" ".join(str(i) for i in message))

"""
45 - Sort List of Lists
46 - Custom key function with 2D Lists
"""
print('------------------ Lesson 45 -> 47 ------------------')


def avg(data: List[int]):
    # print the result to see how it works!
    return sum(data) / len(data)


print(sorted(data, key=avg))
