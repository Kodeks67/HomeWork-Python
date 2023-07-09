def verse_rhythm(str_verse):
    list_count = []
    res = str_verse.split()
    if len(res) <= 1:
        print('Рифмы нет')
    else:
        for i in range(len(res)):
            count = 0
            res_word = res[i]
            for j in range(len(res_word)):
                if is_vowel(res_word[j]):
                    count += 1
            list_count.append(count)
        print(res, list_count)
    return list_count


def is_vowel(some_char):
    if some_char in 'ауоыиэяюёе':
        return True
    else:
        return False


def has_rhythm(list_count):
    flag = False
    for i in range(len(list_count)):
        if list_count[i] == list_count[i - 1]:
            flag = True
        else:
            flag = False
            break
    if flag:
        print('Парам пам-пам')
    else:
        print('Пурум пум-пум')


str_ver = input('Напиши фразу в строчку: ')
has_rhythm(verse_rhythm(str_ver))
