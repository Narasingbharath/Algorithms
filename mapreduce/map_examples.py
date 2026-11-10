numbers = [1, 2, 3, 4, 5]

#Python given an array add each element by 2
def add_num(n):
    return n + 2

result = list(map(add_num, numbers))
print(result)


#Given an array multiply by 5
def mult_num(n):
    return n * 5

result = list(map(mult_num, numbers))
print(result)


#Given an array square it
def num_square(n):
    return n * n

result = list(map(num_square, numbers))

print(result)

