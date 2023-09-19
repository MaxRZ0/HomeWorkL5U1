while True:
    number = int(input('Введите число от 0 до 100.000: '))

    if number <= 0 or number >= 100000:
        print('Введено некорректное число, повторите попытку')
        continue
    else:
        if number == 2 or number == 3:
            print('Введеное число является целым')
            break
        elif number % 2 != 0 and number % 3 != 0:
            print('Введеное число является целым')
            break
        else:
            print('Число не является целым')
            break
