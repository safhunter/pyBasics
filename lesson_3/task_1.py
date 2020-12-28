def division(dividend, divider):
    try:
        return dividend/divider
    except ZeroDivisionError:
        return None


while True:
    try:
        arg_1 = int(input('Введите делимое x: '))
        arg_2 = int(input('Введите делитель y: '))
        break
    except ValueError:
        print('Введите число!')

try:
    print(f'x/y =  {division(arg_1, arg_2):.3f}')
except TypeError:
    print('Результат не определен!')
