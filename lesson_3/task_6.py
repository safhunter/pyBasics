def int_func(string):
    """ Возвращает слово с заглавной буквы, просто обертка для str.capitalize()

        Позиционные параметры:
        string -- строка

    """
    return string.capitalize()


words = input('Введите текст: ').split()
try:
    for index, word in enumerate(words):
        words[index] = int_func(word)
    print(" ".join(words))
except (AttributeError, TypeError):
    print('Что-то пошло не так')
