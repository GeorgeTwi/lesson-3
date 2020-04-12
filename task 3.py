"""В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
 Сами минимальный и максимальный элементы в сумму не включать."""

MAX = 0

list_numbers = [12, 65, 55, 72, 44, 2, 20, 24, 15, 25, 90, 15, 10]

for idx in list_numbers:
    if MAX < idx:
        MAX = idx

MIN = MAX

for idx in list_numbers:
    if idx < MIN:
        MIN = idx

sum = 0
for num in list_numbers[list_numbers.index(MIN) + 1:list_numbers.index(MAX)]:
    sum += num

print(sum)
