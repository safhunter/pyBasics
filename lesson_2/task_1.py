test_list = ['1', 13, True, (1, 2), {1, 5, 7}, ['My', 'Name'], None, {'1': 1, '2': 2}]

for index, item in enumerate(test_list):
    print(f'Item[{index}] = {item} is {type(item)} type')
