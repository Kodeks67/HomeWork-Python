def arithmetic_progression(number, difference, quantity_number):
    list_1 = []
    for i in range(quantity_number):
        list_1.append(number)
        number += difference
    return list_1


print(arithmetic_progression(7, 10, 5))
