"""втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа."""

list_numbers = [8, 3, 15, 6, 4, 2, 7, 22, 12, 9]
list_index = []

for num in list_numbers:
    if num % 2 == 0:
        list_index.append(list_numbers.index(num))

print(list_index)