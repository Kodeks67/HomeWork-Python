def fibonacci(number):
    fibo_1, fibo_2 = 0, 1
    index = 1
    while fibo_2 < number:
        fibo_1, fibo_2 = fibo_2, fibo_1 + fibo_2
        index += 1
    if number == fibo_2:
        return index
    else:
        return -1


num = int(input('Введите число на проверку фибоначчи: '))
print(fibonacci(num))

