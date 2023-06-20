from random import randint


def various_numbers(len_num):
    count = 0
    list_1 = [randint(-10, 10) for _ in range(len_num)]
    for i in range(len(list_1)):
        for j in range(i + 1, len(list_1)):
            if list_1[i] > list_1[j]:
                list_1[i], list_1[j] = list_1[j], list_1[i]
        if list_1[i] != list_1[i - 1]:
            count += 1
    print(list_1, count, end='\n')


number = int(input('Введите размер списка: '))
various_numbers(number)


def various_num(len_num):
    count = 0
    list_1 = [randint(-10, 10) for _ in range(len_num)]
    list_1.sort()
    for i in range(len(list_1)):
        if list_1[i] != list_1[i - 1]:
            count += 1
    print(list_1, count, end='\n')


num = int(input('Введите размер списка: '))
various_num(num)
