# Способ решения задачи №1

def SummaThreeDigitNumber(number):
    FirstNumber = number // 100
    SecondNumber = (number // 10) % 10
    ThirdNumber = number % 10
    print(f"сумма трехзначного числа = {FirstNumber + SecondNumber + ThirdNumber}")


numbers = int(input())
SummaThreeDigitNumber(numbers)


# Способ решения задачи №2

def SummaThreeDigitNumberSTR(num):
    num = str(num)
    FirstNumberSTR = int(num[0])
    SecondNumberSTR = int(num[1])
    ThirdNumberSTR = int(num[2])
    print(f"сумма трехзначного числа = {FirstNumberSTR + SecondNumberSTR + ThirdNumberSTR}")


SummaThreeDigitNumberSTR(numbers)
