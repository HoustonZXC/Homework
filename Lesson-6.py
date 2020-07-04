# Python 3.8.2
# OS - 64bit Windows
from random import random
import sys

def count_size(x):
    size = sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                size += sys.getsizeof(key)
                size += sys.getsizeof(value)
        elif not isinstance(x, str):
            for item in x:
                size += sys.getsizeof(item)
    return size

# 1
x = int(input('Введите число: '))
y = 0
z = 1
for i in range(x):
    y = y + z
    z = z / -2
print(f'Ответ: {y}')

sum_1 = 0
list_1 = [x, y, z]
for k in list_1:
    sum_1 += count_size(k)
print(f'{sum_1} байт памяти задействовано')
# 46 байт памяти задействовано (x = 5)

# 2
x = int(input("Кол-во чисел:  "))
y = int(input("Цифра для подсчета: "))
count = 0
for i in range(1, x + 1):
    z = int(input("Число " + str(i) + ": "))
    while z > 0:
        if z % 10 == y:
            count += 1
        z = z // 10

print(f'Цифра: {y}; Повторяется: {count} раз(а)')

sum_2 = 0
list_2 = [x, y, count, z]
for j in list_2:
    sum_2 += count_size(j)
print(f'{sum_2} байт памяти задействовано')
# Кол-во чисел:  2
# Цифра для подсчета: 5
# Число 1: 12345567
# Число 2: 555555
# 54 байт памяти задействовано

# 3

index = []
x = 10
array = [0] * x
for i in range(x):
    array[i] = int(random() * 10)
    if array[i] % 2 == 0:
        index.append(i)
print(array)
print(index)

sum_3 = 0
list_3 = [index, x, array]
for l in list_3:
    sum_3 += count_size(l)
print(f'{sum_3} байт памяти задействовано')
# 306 байт памяти задействовано
