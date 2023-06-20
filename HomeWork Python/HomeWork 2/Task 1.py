from random import randint


def inverted_coins(money):
    count = 0
    for i in range(money):
        rand_money = randint(0, 1)
        print(rand_money, end=' ')
        if rand_money == 0:
            count += 1
    print(f'\n{count}')


mon = int(input('Введите число: '))
inverted_coins(mon)
