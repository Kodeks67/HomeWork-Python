# numberStudents1 = int(input('Введите кол-во учеников в 1 классе: '))
# numberStudents2 = int(input('Введите кол-во учеников в 2 классе: '))
# numberStudents3 = int(input('Введите кол-во учеников в 3 классе: '))
# print(round((numberStudents1 + numberStudents2 + numberStudents3) / 2))


# def NumberDesks(number1, number2, number3):
#     print(round((number1 + number2 + number3) / 2))
#
#
# numberStudents1 = int(input('Введите кол-во учеников в 1 классе: '))
# numberStudents2 = int(input('Введите кол-во учеников в 2 классе: '))
# numberStudents3 = int(input('Введите кол-во учеников в 3 классе: '))
# NumberDesks(numberStudents1, numberStudents2, numberStudents3)


numberStudents1 = int(input('Введите кол-во учеников в 1 классе: '))
numberStudents2 = int(input('Введите кол-во учеников в 2 классе: '))
numberStudents3 = int(input('Введите кол-во учеников в 3 классе: '))
print(round((numberStudents1 + (numberStudents1 % 2 == 0) + numberStudents2 + (numberStudents1 % 2 == 0) +
             numberStudents3 + (numberStudents1 % 2 == 0)) / 2))
