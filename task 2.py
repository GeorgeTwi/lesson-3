"""В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""

MAX = 0

list = [18, 33, 73, 54, 16, 38, 2, 79, 44, 58, 7, 46, 92, 33, 51]
print(list)

for idx in list:
    if MAX < idx:
        MAX = idx

MIN = MAX

for idx in list:
    if idx < MIN:
        MIN = idx

list[list.index(MAX)], list[list.index(MIN)] = list[list.index(MIN)], list[list.index(MAX)]
print(list)

