from random import randint


def next_day(day):
    result = 0
    temp = 0
    max_next_day = 0
    for i in range(day):
        temp += randint(-3, 3)
        if temp > 0:
            result += 1
            if result > max_next_day:
                max_next_day = result
        else:
            result = 0
        print(temp, end=' ')
    print('\n' + str(max_next_day))


day = int(input())
next_day(day)
