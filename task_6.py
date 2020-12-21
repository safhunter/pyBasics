import math
initial_dist = 0.0
goal_dist = 0.0
days = 0
PROGRESS = 1.1
MAX_DAY_DIST = 25902068371.2

while True:
    try:
        initial_dist = float(input('Введите начальный результат в км: '))
        # Для того чтобы пробежать 25902068371.2 км за 24 часа нужно развить скорость света в вакууме
        if initial_dist >= MAX_DAY_DIST:
            print('По-моему кто-то врет ;)')
        elif initial_dist > 0:
            break
    except ValueError:
        print('Введите число!')

while True:
    try:
        goal_dist = float(input('Введите желаемый результат в км: '))
        if goal_dist > 0:
            break
    except ValueError:
        print('Введите число!')

if goal_dist >= MAX_DAY_DIST:
    print(f'Извините, цель не достижима')
else:
    days = 1 + math.ceil(math.log(goal_dist / initial_dist, PROGRESS))
    print(f'Необходимо {days} дней для достижения результата')

