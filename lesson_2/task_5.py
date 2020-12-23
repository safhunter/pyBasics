rating_list = []

while True:
    try:
        user_input = input('Введите натуральное число (для выхода введите пустую строку): ')
        if user_input == '':
            break
        else:
            number = int(user_input)
            if number > 0:
                index = 0
                for num in rating_list:
                    if num < number:
                        break
                    index += 1
                rating_list.insert(index, number)
                print(f'Текущий рейтинг: {rating_list}')
    except ValueError:
        print('Введите число!')
# for obj in rating_list:
#     print(id(obj))
