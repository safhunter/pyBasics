import random as rnd
from collections import OrderedDict


init_list = [rnd.randrange(0, 20) for i in range(10)]
res_dict = OrderedDict()
res_list = []

for item in init_list:
    res_dict[item] = res_dict.get(item, 0) + 1

for key in res_dict:
    if res_dict[key] == 1:
        res_list.append(key)

print(f'Исходный список: {init_list}')
print(f'Итоговый список: {res_list}')
