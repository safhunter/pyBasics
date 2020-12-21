name = 'default'
age = 18

name = input('Введите свое имя: ')
while True:
    try:
        age = int(input('Введите свой возраст: '))
        if age >= 0:
            break
    except ValueError:
        print('Введите число!')

if age < 18:
    print(f'Привет, {name}')
else:
    print(f'Привествую вас, {name}')
