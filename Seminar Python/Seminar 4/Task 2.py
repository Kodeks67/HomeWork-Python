n = input()
list_1 = []
dict_count = {}
for i in n:
    dict_count[i] = dict_count.get(i, 0) + 1
    if dict_count.get(i) < 2:
        print(i, end=' ')
    else:
        print()
