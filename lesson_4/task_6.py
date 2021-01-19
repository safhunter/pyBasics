import itertools as it
from random import randrange

while True:
    try:
        start = int(input('Введите начальное число < 20: '))
        break
    except ValueError:
        print('Введите число!')

for i in it.count(start):
    if i > 20:
        break
    else:
        print(i)
print(f'------------------- Работа cycle() ----------------------')
init_list = [randrange(0, 100) for i in range(7)]
print(init_list)

stop = 10
for el in it.cycle(init_list):
    if stop <= 0:
        break
    print(el)
    stop -= 1
