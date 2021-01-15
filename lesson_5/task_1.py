try:
    with open('task_1.txt', 'w', encoding='utf-8') as f:
        while True:
            user_str = input('Введите строку: ')
            if user_str == '':
                break
            f.write(user_str + '\n')
except IOError:
    input(f'Ошибка чтения файла. Нажмите Enter для выхода')
    exit()
