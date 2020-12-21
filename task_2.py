hours = 0
minutes = 0
seconds = 0

while True:
    try:
        time_sec = int(input('Введите время в секундах: '))
        break
    except ValueError:
        print('Введите число!')

hours = time_sec // 3600
minutes = (time_sec % 3600) // 60
seconds = time_sec % 60

print(f'Итоговое время {hours:02}:{minutes:02}:{seconds:02}')
