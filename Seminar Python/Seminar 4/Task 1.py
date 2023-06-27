import re

text = 'Единственное исключение — некоторые продавцы распродадут свой товар, купленный по старому курсу, по старым же ценам.'

reg = re.compile('[^а-яА-Яa-zA-z ]')
rep = reg.sub('', text).split()
print(len(set(rep)))
