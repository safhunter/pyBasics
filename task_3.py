n = 0
term_1 = 0
term_2 = 0
term_3 = 0

while True:
    try:
        n = input('Введите число n больше 0: ')
        term_1 = int(n)
        if term_1 > 0:
            break
    except ValueError:
        print('Введите число!')

term_2 = int(n * 2)
term_3 = int(n * 3)

print(f'Сумма {n} + {n + n} + {n + n + n} = {term_1 + term_2 + term_3}')
