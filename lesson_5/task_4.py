numerals_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
}
result_list = []
try:
    with open('task_4_1.txt', encoding='utf-8') as f:
        for i, line in enumerate(f.readlines()):
            try:
                values = line.split()
                values[0] = numerals_dict[values[0].lower()].capitalize()
                result_list.append(' '.join(values) + '\n')
            except (IndexError, KeyError):
                print(f'Некорректное значение в строке {i+1}')
    f = open('task_4_2.txt', 'w', encoding='utf-8')
    f.writelines(result_list)
    f.close()
except IOError:
    input(f'Ошибка чтения файла. Нажмите Enter для выхода')
    exit()
