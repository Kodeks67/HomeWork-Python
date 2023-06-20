def guess_number(num1, num2):
    first_num = 0
    second_num = 0
    for i in range(1, num1):
        if num1 - i == num2 // i:
            first_num += num1 - i
            second_num += num1 - first_num
            if num1 == first_num + second_num and num2 == first_num * second_num:
                print(second_num, first_num)
                break
            else:
                print('Числа не подходят')


fir_num = int(input('Введите 1 подсказку: '))
sec_num = int(input('Введите 2 подсказку: '))
guess_number(fir_num, sec_num)
