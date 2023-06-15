# def calculate_total_wagons(i, j):
#     if i < j:
#         from_head = True
#     elif i > j:
#         from_head = False
#     else:
#         print("Ошибка: Номер вагона Вити совпадает с номером его положения.")
#         return None
#
#     if from_head:
#         total_wagons = j + (j - i)
#     else:
#         total_wagons = i + (i - j)
#
#     return total_wagons
#
#
# i = int(input("Введите номер вагона, в котором сел Витя (i): "))
# j = int(input("Введите номер вагона, указанный в вагоне (j): "))
#
# total_wagons = calculate_total_wagons(i, j)
#
# if total_wagons is not None:
#     print("Общее количество вагонов в электричке:", total_wagons)


# a = int(input())
# b = int(input())
#
# if a == b:
#     print("равен номеру вагона")
# else:
#     print(f"мин кол-во вагонов {a + b - 1}")

