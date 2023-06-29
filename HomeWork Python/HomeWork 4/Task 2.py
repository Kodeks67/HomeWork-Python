from random import randint


def max_number_berries(len_number):
    list_2 = []
    list_1 = [randint(0, 10) for _ in range(len_number)]
    print(f'Рандомный массив: {list_1}')
    for i in range(len(list_1)):
        list_2.append(list_1[i] + list_1[i - 1] + list_1[i - 2])
    print(f'Всего число ягод можно собрать: {max(list_2)}')


len_num = int(input())
max_number_berries(len_num)
