def division(dividend, divider):
    """ Возвращает частное от деления.

        В случае ошибки возвращает None
        Позиционные параметры:
        dividend -- делимое
        divider -- делитель

    """
    try:
        return dividend/divider
    except ZeroDivisionError:
        return None


while True:
    try:
        arg_1 = float(input('Введите делимое x: '))
        arg_2 = float(input('Введите делитель y: '))
        break
    except ValueError:
        print('Введите число!')

try:
    print(f'x/y =  {division(arg_1, arg_2):.3f}')
except TypeError:
    print('Результат не определен!')
