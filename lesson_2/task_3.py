seasons_list = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
seasons_dict = {
    1: 'Зима',
    2: 'Зима',
    3: 'Весна',
    4: 'Весна',
    5: 'Весна',
    6: 'Лето',
    7: 'Лето',
    8: 'Лето',
    9: 'Осень',
    10: 'Осень',
    11: 'Осень',
    12: 'Зима'
}

while True:
    try:
        month_num = int(input('Введите порядковый номер месяца: '))
        if 0 < month_num < 13:
            break
    except ValueError:
        print('Введите число!')
print(f'Время года: {seasons_list[month_num-1]}')
print(f'Время года: {seasons_dict[month_num]}')
