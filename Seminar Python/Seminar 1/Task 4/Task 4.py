# def LeapYear(number):
#     if number % 4 == 0 and number % 100 != 0 and number % 400 != 0:
#         print('Является ли високосным год : Yes')
#     else:
#         print('Является ли високосным год : NO')
#
#
# number = int(input('Введите год: '))
# LeapYear(number)


number = int(input('Введите год: '))

if number % 4 == 0 and number % 100 != 0 and number % 400 != 0:
    print('Является ли високосным год : Yes')
else:
    print('Является ли високосным год : NO')


