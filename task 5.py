"""Определить, какое число в массиве встречается чаще всего."""

COUNT = 1
num = None

list_numbers = [11, 13, 87, 23, 99, 99, 9, 71, 70, 23, 92, 23]

for i in range(len(list_numbers) - 1):
    temp_count = 1
    for idx in range(i + 1, len(list_numbers)):
        if list_numbers[i] == list_numbers[idx]:
            temp_count += 1
    if temp_count > COUNT:
        COUNT = temp_count
        num = list_numbers[i]

print(f'Число {num} повторялось {COUNT} раз(а)')