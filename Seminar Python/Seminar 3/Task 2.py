from random import randint


def shift_list(len_num, shift_num):
    list_1 = [randint(-10, 10) for _ in range(len_num)]
    print(f'Начальный массив: {list_1}')
    return list_1[shift_num:] + list_1[:shift_num]


len_numbers = int(input('Введите размер массива: '))
shift_number = int(input('Введите сдвиг: '))
print("Конечный массив: ", shift_list(len_numbers, shift_number))
