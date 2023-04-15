# Задача 16+18: Рассчитать частоту встречаемости числа в списке, либо (если такого числа
# в списке нет) найти ближайшее к нему число.

import random

size = int(input('Укажите размер списка: '))
my_list = [random.randint(0, 10) for _ in range(size)]
print(my_list)
number_x = int(input('Введите число в диапазоне от 0 до 10, которое надо найти в списке: '))
frequency_of_a_number = my_list.count(number_x)
print(f'Такое число встречается {frequency_of_a_number} раз')
the_nearest_number = 0
if frequency_of_a_number == 0:
    print('Такого числа нет в списке.')
    min_difference = 100
    for i in range(size):
        difference = abs(my_list[i] - number_x)
        if difference < min_difference:
            min_difference = difference
            the_nearest_number = my_list[i]
    print(f'Ближайшее к нему число - это {the_nearest_number}')
