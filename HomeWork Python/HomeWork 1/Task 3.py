def LuckyTicket(number):
    if (number // 100000) % 10 + (number // 10000) % 10 + (number // 1000) % 10 == (number // 100) % 10 + (number % 100) // 10 + number % 10:
        print("Билетик Счастливый УРА!")
    else:
        print("Билетик не счастливый")


number = int(input())
LuckyTicket(number)
