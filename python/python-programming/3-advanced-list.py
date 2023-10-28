"""
INPUT, STACKS, QUEUES

[37] - Fill List from user input
[38] - Loop to fill List from user input

---

Data Structure is just a way of storing data

[39] - Create a Stack - Use a List as a Stack
>>> foods.pop() # remove the item on the right

PHILO: First In Last Out | LIFO: Last In First Out

[40] - Create a Queue - Use a List as a Queue
>>> foods.pop(0) # remove the item on the left

FIFO: First In First Out
"""
print('------------------ Lesson 37 -> 41 ------------------')

print('Tell us your favorite veggies.')
data = input('Hit enter after each food. r to remove, q to quit')

foods = []

while True:
    data = input()
    if str.lower(data) == 'q':
        break
    elif str.lower(data) == 'r':
        print('Removed:', foods.pop())
        continue
    foods.append(data)
    print('Data:', foods)

for food in foods:
    print('You said:', food)
