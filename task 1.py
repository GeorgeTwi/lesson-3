"""В диапазоне натуральных чисел от 2 до 99 определить,
 сколько из них кратны каждому из чисел в диапазоне от 2 до 9."""

COUNT = 2
c = 2

list = []

numbers = {}

while COUNT != 10:
    for i in range(2, 100):
        if i % COUNT == 0:
            list.append(i)
    numbers.update({COUNT: list.copy()})
    COUNT += 1
    list.clear()

for key, val in numbers.items():
    print(f'Числа кратные {key}: {val}')
