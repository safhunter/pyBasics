def pow_func(x, y):
    """ Возвращает результат операции возведения x в степень y.

        В случае ошибки возвращает None
        Позиционные параметры:
        x -- действительное > 0
        y -- целое

    """
    try:
        result = 1.0
        # Случай отрицательной степени
        if y < 0:
            x = 1/x
            y = -y
        while y > 0:
            # Если последняя цифра показателя степени в двоичной СИ - 1
            if (y & 1) == 1:
                result *= x
                y = y - 1
            else:
                x *= x
                y = y >> 1
        return result
    except TypeError:
        return None


print(str(pow_func(1.5, -25)))
