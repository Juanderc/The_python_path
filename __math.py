from operator import add, mul
from functools import reduce

numbers = [9, 3, 4, 7]


def my_add(a, b):
    return a + b


print(reduce(my_add, numbers))

print("---------------------max_number-----------------------\n")
max_number, *rest = numbers
for num in rest:
    if num > max_number:
        max_number = num

print(max_number)

# (*) is used to store the remaining value
# in the initial loop max_number = 3 and
# *rest = [4,7,9]
