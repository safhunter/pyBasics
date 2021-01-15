import re
from functools import reduce


def get_hours(data: str) -> int:
    hours = re.findall(r' \d*\(', data)
    result = 0
    for num in hours:
        result += int(num[1:-1])
    return result


subjects = {}
try:
    with open('task_6.txt', encoding='utf-8') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            try:
                subjects[re.match(r'\w*:', line).group(0)[:-1]] = get_hours(line)
            except (KeyError, IndexError):
                print(f'Некорректные данные в строке {i}')
    print(subjects)
except IOError:
    input(f'Ошибка чтения файла. Нажмите Enter для выхода')
    exit()
