try:
    with open('task_2.txt', encoding='utf-8') as f:
        lines = f.readlines()
        print(f'Количество строк в файле {f.name}: {len(lines)}')
except IOError:
    input(f'Ошибка чтения файла. Нажмите Enter для выхода')
    exit()
for i, line in enumerate(lines):
    print(f'Количество слов строке {i+1}: {len(line.split())}')
