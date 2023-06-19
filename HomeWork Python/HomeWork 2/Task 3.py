def integers(number):
    for i in range(0, number):
        if 2 ** i < number:
            print(2 ** i, end=' ')


num = int(input('Введите число: '))
integers(num)
