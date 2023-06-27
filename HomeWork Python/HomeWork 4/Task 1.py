# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания
# все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
from random import randint


def search_same_number(first_number, second_number):
    list_1 = [randint(-10, 10) for _ in range(first_number)]
    list_2 = [randint(-10, 10) for _ in range(second_number)]
    numbers_1 = list(set(sorted(list_1)))
    numbers_2 = list(set(sorted(list_2)))
    num = 0
    for i in range(len(numbers_1)):
        for j in range(len(numbers_2)):
            if numbers_1[i] == numbers_2[j]:
                count = numbers_1[i]
                num += 1
                print(f'Совпадение {num}: {count}')
    print(list_1, list_2, end='\n')


search_same_number(7, 7)
