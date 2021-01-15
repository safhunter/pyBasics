def sum_elements(numbers):
    """ Возвращает сумму элементов списка и флаг успешного прохода всех элементов.

        В случае, если какой-то элемент не удалось просуммировать, возвращает False и уже посчитанную сумму
        предыдущих элементов.
        (list) -> bool, int
        Позиционные параметры:
        number -- список чисел

    """
    result = 0
    try:
        for number in numbers:
            result += int(number)
    except (ValueError, TypeError):
        print('Вы ввели не число')
        return False, result
    return True, result


total_sum = 0
next_step = True
while next_step:
    num_list = input(f'Введите числа через пробел: {total_sum} ').split()
    next_step, tmp_sum = sum_elements(num_list)
    total_sum += tmp_sum

print(f'Итоговая сумма: {total_sum}')
