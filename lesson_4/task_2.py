import random as rnd

size = rnd.randrange(2, 100)
init_list = []
res_list = []
init_list.append(rnd.randrange(0, 1000))

for i in range(1, size-1):
    init_list.append(rnd.randrange(0, 1000))
    if init_list[i] > init_list[i-1]:
        res_list.append(init_list[i])

print(f'Исходный список: {init_list}')
print(f'Итоговый список: {res_list}')
