input_list = []
result_list = []

inverse = False
while True:
    user_input = input('Введите следующий элемент списка (для прекращения, введите пустую строку): ')
    if user_input != '':
        input_list.append(user_input)
        if not inverse:
            result_list.append(user_input)
        else:
            result_list.append(result_list[-1])
            result_list[-2] = user_input
        inverse = not inverse
    else:
        break
print(f'Исходный список: {input_list}')
print(f'Инвертированный список: {result_list}')
