import random

# Random integer from 1 to 10
print(random.randint(1, 10))

# Random number between 0 and 1
print(random.random())

# Random choice from a list
fruits = ["apple", "banana", "mango"]
print(random.choice(fruits))

# Shuffle a list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)