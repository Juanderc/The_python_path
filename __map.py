# map
def plus(x):
    x + x


lista = [1, 2, 3, 4, 5]

result = map(plus, [1, 2, 3, 4, 5])
print(list(result))


def myfunc(n):
    return len(n)


x = map(myfunc, ('apple', 'banana', 'cherry'))
print(list(x))
