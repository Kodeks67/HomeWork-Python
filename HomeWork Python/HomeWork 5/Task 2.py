def sum_recursive(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return sum_recursive(a + 1, b - 1)


print(sum_recursive(5, 5))
