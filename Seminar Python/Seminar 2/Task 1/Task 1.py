def factorial(number):
    count = 1
    while number > 0:
        count *= number
        number -= 1
    print(count)

n = 5
factorial(n)