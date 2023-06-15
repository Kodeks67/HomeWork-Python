def NumbaerLogs(number):
    FirstNumbaer = int(round(number / 6))
    SecondNumber = number - FirstNumbaer * 2
    print(f"Петр сделал журналов: {FirstNumbaer}, Катя сделала: {SecondNumber}, Сергей сделал: {FirstNumbaer}")


number = int(input('Введите общее кол-во журналов было сделано: '))
NumbaerLogs(number)

