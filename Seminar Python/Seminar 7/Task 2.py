def same_by(characteristic, objects):
    return len(objects) == len(list(filter(characteristic, objects)))


lst = ['sss', 'eeee', 'tttt', 'qqqq']
print(same_by(lambda x: len(x) == 4, lst))
