def my_func(arg_1, arg_2, arg_3):
    """ Возвращает сумму двух наибольших чисел.

        В случае ошибки возвращает None
        Позиционные параметры:
        arg_1 -- число 1
        arg_2 -- число 2
        arg_3 -- число 3

    """
    try:
        return arg_1 + arg_2 + arg_3 - min(arg_1, arg_2, arg_3)
    except TypeError:
        return None


print(str(my_func(-1, 32, -103)))
