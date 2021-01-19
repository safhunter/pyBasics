from random import randrange
from functools import reduce

try:
    with open('task_5.txt', 'w+', encoding='utf-8') as f:
        f.writelines(map((lambda x: str(x) + ' '), [randrange(0, 100) for i in range(1, 101)]))
        f.seek(0)
        print(f'Сумма чиасел равна: {reduce(lambda a, b: int(a) + int(b), f.readlines()[0].split())}')
except IOError:
    input(f'Ошибка чтения файла. Нажмите Enter для выхода')
    exit()

