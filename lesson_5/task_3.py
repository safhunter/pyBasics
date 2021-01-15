try:
    with open('task_3.txt', encoding='utf-8') as f:
        lines = f.readlines()
except IOError:
    input(f'Ошибка чтения файла. Нажмите Enter для выхода')
    exit()

print(f'Сотрудники с окладом менее 20000:')
total = 0.0
for i, line in enumerate(lines):
    user_data = line.split()
    try:
        salary = float(user_data[1])
        total += salary
        if salary < 20000:
            print(user_data[0])
    except (ValueError, IndexError):
        print(f'Неверный формат записи в строке {i+1}: {line}')
try:
    print(f'Средня зарплата = {total/len(lines):.2f}')
except ZeroDivisionError:
    print(f'Файл пуст')
