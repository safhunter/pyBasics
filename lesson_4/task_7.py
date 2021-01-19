import math


def func(n):
    for i in range(1, n+1):
        yield math.factorial(i)


for el in func(10):
    print(el)

