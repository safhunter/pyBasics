n_str = ''
n = 0
max_digit = 0

while True:
    try:
        n_str = input('Введите число n больше 0: ')
        n = int(n_str)
        if n > 0:
            break
    except ValueError:
        print('Введите число!')

i = 0
# Начиная с 7-значных чисел вероятность получить max_digit = 9, превышает вероятность того что max_digit < 9
# поэтому есть смысл проверять max_digit на каждо шаге. Для коротких чисел это практически не скажется
# на производительности, а для длинных поможет снизить среднее число шагов цикла.
# Рассуждения верны только в том случае, когда цифры в числах имеют равномерное распределение вероятности.
while i < len(n_str) and (max_digit < 9):
    if int(n_str[i]) > max_digit:
        max_digit = int(n_str[i])
    i += 1

print(f'Максимальная цифра вашего чиасла: {max_digit}')