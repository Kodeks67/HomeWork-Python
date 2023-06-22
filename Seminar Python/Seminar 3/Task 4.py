from random import randint

len_num = int(input('Введите размер массива: '))
print(list_1 := [randint(-10, 10) for _ in range(len_num)])
print(len([i for i in range(1, len(list_1)) if list_1[i - 1] < list_1[i]]))
