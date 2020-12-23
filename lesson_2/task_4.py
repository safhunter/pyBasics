result_list = input('Введите строку: ').split()

for index, item in enumerate(result_list):
    print(f'{index}: {item[:10:]}')
