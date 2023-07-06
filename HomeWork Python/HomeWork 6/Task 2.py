from random import randint


def index_elements_list(min_num, max_num, len_list):
    list_2 = []
    list_1 = [randint(-10, 10) for _ in range(len_list)]
    print(list_1)
    for i in range(len(list_1)):
        if min_num <= list_1[i] <= max_num:
            list_2.append(i)
    return list_2


print(index_elements_list(-2, 5, 20))
