product_list = []
prop_dict = {}
analytics_dict = {
    "название": [],
    "цена": [],
    "количество": [],
    "ед": []
}
product_id = 1

print('Введите информацию о ваших товарах (для прекращения, введите пустую строку разделе "наименование")!')

while True:
    prop_dict["название"] = input(f'Введите наименование товара {product_id}: ')
    if prop_dict["название"] == '':
        break
    try:
        prop_dict["цена"] = int(input(f'Введите цену товара {product_id}: '))
        if prop_dict["цена"] <= 0:
            continue
        prop_dict["количество"] = int(input(f'Введите количество товара {product_id}: '))
        if prop_dict["количество"] < 0:
            continue
    except ValueError:
        print('Неверное значение')
    prop_dict["ед"] = input(f'Введите еденицы измерения товара {product_id}: ')
    product_list.append(tuple([product_id, prop_dict.copy()]))
    for key in analytics_dict:
        analytics_dict[key].append(prop_dict[key])
    product_id += 1

print(f'Список товаров: [\n{chr(10).join(map(str, product_list))}\n]')
print(f'Аналитика: {{\n{chr(10).join(map(lambda x: str(x)+": "+str(analytics_dict[x]), analytics_dict))}\n}}')
