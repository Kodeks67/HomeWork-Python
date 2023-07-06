def number_degree(num1, num2):
    if num2 == 0:
        return 1
    elif num2 > 0:
        return num1 * number_degree(num1, num2 - 1)


print(number_degree(1, 0))
