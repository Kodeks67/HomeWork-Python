def find_closest_numbers(list_1, k):
    closest_numbers = []
    min_diff = None

    for num in list_1:
        diff = abs(k - num)

        if not closest_numbers:
            closest_numbers.append(num)
            min_diff = diff
        elif diff <= min_diff:
            if diff < min_diff:
                closest_numbers.clear()
            closest_numbers.append(num)
            min_diff = diff

    return closest_numbers


list_1 = [1, 2, 3, 4, 6,8, 9]
k = 7
closest_num = find_closest_numbers(list_1, k)
print(*closest_num)