# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint
from time import sleep

lower_limit = 0
upper_limit = 1000
number = randint(lower_limit, upper_limit)

trying = 10

print('Приветствую Вас в программе "Угадайка"!')
print('Вам предстоит угадать число, загаданное компьютером, в диапазоне от 0 до 100.000.', flush=True)
sleep(6)
print('Количество попыток ограничено и равняется 10.')
print('Если Вы исчерпаете их все и так и не отгадаете, то Вы проиграли.', flush=True)
print('Каждый неверный ответ, забирает одну попытку.')
sleep(5)
print('Удачи!')

while trying > 0:
    user_number = input(f'Попытка №{11-trying}. Предложите число: ')

    try:
        user_number = int(user_number)
    except:
        trying -= 1
        print('Что-то не то, попробуйье ещё раз.  - 1 попытка, осталось {trying}')

    if number < user_number:
        trying -= 1
        print(f'Введеное число больше загаданного. - 1 попытка, осталось {trying}')
    elif number > user_number:
        trying -= 1
        print(f'Введенное число меньше загаданного. - 1 попытка, осталось {trying}')
    else:
        print(f'Всё верно! Вы смогли угадали с попытки №{11-trying}')
        break
else:
    print(f'Очень жаль, но Вы не смоги отгадать число. Правильный ответ {number}')
