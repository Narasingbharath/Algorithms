from functools import reduce

numbers = [1, 2, 3, 4, 5]

def add_num(a, b):
    return a + b

result = reduce(add_num, numbers)
print(result)


def mul_num(a, b):
    return a * b

result = reduce(mul_num, numbers)
print(result)

def square(a, b):
    return a + (b * b)

result = reduce(square, numbers)
print(result)
