import json

firms_dict = {}
average_profit_dict = {'average_profit': 0}
total_profit = 0
count = 0
try:
    with open('task_7.txt', encoding='utf-8') as f:
        for i, line in enumerate(f.readlines()):
            try:
                words = line.split()
                profit = float(words[2]) - float(words[3])
                firms_dict[words[0]] = round(profit, 2)
                if profit >= 0:
                    total_profit += profit
                    count += 1
            except (IndexError, ValueError):
                print(f'Неверные данные в строке {i}')
    if count > 0:
        average_profit_dict['average_profit'] = round(total_profit/count, 2)
    f = open('task_7.json', 'w', encoding='utf-8')
    json.dump([firms_dict, average_profit_dict], f)
    f.close()
except IOError:
    input(f'Ошибка чтения файла. Нажмите Enter для выхода')
    exit()
