# Способ решения задачи №1
def LuckyTicket(number):
    if (number // 100000) % 10 + (number // 10000) % 10 + (number // 1000) % 10 == (number // 100) % 10 + \
            (number % 100) // 10 + number % 10:
        print("Счастливый билет УРА!!!")
    else:
        print("Не счастливый билетик(")


number = int(input('Введите шестизначное число: '))
LuckyTicket(number)


# Способ решения задачи №2

def LuckyTicketSTR(number):
    num = str(number)
    num1, num2, num3, num4, num5, num6 = int(num[0]), int(num[1]), int(num[2]), int(num[3]), int(num[4]), int(num[5])
    if num1 + num2 + num3 == num4 + num5 + num6:
        print('Счастливый билет УРА!!!')
    else:
        print('Не счастливый билетик(')


LuckyTicketSTR(number)
