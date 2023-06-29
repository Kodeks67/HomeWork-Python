def reverse_number(num):
    if num == 0:
        return ''
    char = input('Введите что-то: ')
    return reverse_number(num - 1) + char


print(reverse_number(5))
