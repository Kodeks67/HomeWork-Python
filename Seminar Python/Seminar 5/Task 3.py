# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

def simplicity_check(num):
    for i in range(2, num):
        if num % i == 0:
            return -1
    return num


print(simplicity_check(10))
