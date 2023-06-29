# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
import random

print(marks := [random.randint(1, 10) for _ in range(10)])

max_mark = max(marks)
min_mark = min(marks)

print([mark if mark != max_mark else min_mark for mark in marks])