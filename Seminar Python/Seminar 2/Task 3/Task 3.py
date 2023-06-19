from random import randint


def mas_watermelon(num_watermelon):
    max_ = 1
    min_ = 20
    for i in range(num_watermelon):
        rand_mas = randint(1, 20)
        print(rand_mas)
        if rand_mas > max_:
            max_ = rand_mas
        if rand_mas < min_:
            min_ = rand_mas
    return min_, max_


num_watermelon = int(input())
print(mas_watermelon(num_watermelon))
