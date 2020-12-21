profit = 0.0
income = 0.0
costs = 0.0
staff_count = 0;

while True:
    try:
        income = float(input('Введите ваш доход: '))
        if income >= 0:
            break
    except ValueError:
        print('Введите число!')

while True:
    try:
        costs = float(input('Введите ваши издержки: '))
        if costs >= 0:
            break
    except ValueError:
        print('Введите число!')

profit = income - costs
if profit >= 0:
    print(f'Ваша прибыль составила: {round(profit, 2)}')
    print(f'Ваша рентабельность выручки составила: {round(100 * profit / income, 1)}%')
    while True:
        try:
            staff_count = int(input('Введите количество сотрудников: '))
            if staff_count > 0:
                break
            elif staff_count == 0:
                staff_count = 1
                break
        except ValueError:
            print('Введите число!')
    print(f'Прибыль на одного сотрудника составила: {round(profit / staff_count, 2)}')
else:
    print(f'Ваш убыток составил: {round(-1 * profit, 2)}')

