while True:
    user_input = input('Введите целое число от 0 до 100.000: ')
    try:
        number = int(user_input)
    except:
        print('Введены некорректные данные, повторите попытку')
        continue

    if number < 0 or number > 100000:
        print('Введено некорректное число, повторите попытку')
        continue
    else:
        if number == 1:
            print('Число не является простым')
            break
        elif number == 2 or number == 3:
            print('Введеное число является простым')
            break
        elif number % 2 != 0 and number % 3 != 0:
            print('Введеное число является простым')
            break
        else:
            print('Число не является простым')
            break
