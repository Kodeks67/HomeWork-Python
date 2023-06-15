def ChekingChocolate(num1, num2, num3):
    if num1 < num2 * num3 and num3 % num1 == 0 or num3 % num2 == 0:
        print('YES')
    else:
        print('NO')


num1 = int(input())
num2 = int(input())
num3 = int(input())
ChekingChocolate(num1, num2, num3)