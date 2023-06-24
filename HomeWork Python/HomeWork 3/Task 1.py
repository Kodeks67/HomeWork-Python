from random import randint


def search_number(len_list, quantity_num):
    count = 0
    list_1 = [randint(-10, 10) for _ in range(len_list)]
    list_1.sort()
    for i in range(len(list_1)):
        if quantity_num == list_1[i - 1]:
            count += 1
    print(list_1, count, end='\n')


len_list = int(input('Введите размер массива: '))
quantity_num = int(input('Введите число: '))
search_number(len_list, quantity_num)


