# Loop

# while
# for
# range()
# enumerate()

nums = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

for num in nums.values():
    num += 1
    print(num)

values = ((10, 20), ['Jose', 'Daniel'], {'a': 2, 'b': 3})
print(type(values[2]))
for val1, val2 in values:
    print(val1, val2)


for val in range(1, 10):
    print(val)


num = [1, 2, 3, 4, 5]

for ind in range(len(num)):
    print("Index:", ind, "Value:", num[ind])
