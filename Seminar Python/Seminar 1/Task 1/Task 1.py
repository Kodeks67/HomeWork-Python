# import math
#
#
# def resultDay(number1, number2):
#     print(math.ceil(number2 / number1))
#
#
# n = int(input('Введите число сколько проедет машина: '))
# m = int(input('Введите число сколько надо проехать: '))
# resultDay(n, m)

n = int(input('Введите число сколько проедет машина за день: '))
m = int(input('Введите число сколько надо проехать всего: '))
print(f'Сколько дней надо проехать: {(m + n -1) // n}')
