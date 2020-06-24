# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

x = [0] * 8
for i in range(2, 100):
    for k in range(2, 10):
        if i % k == 0:
            x[k - 2] = x[k - 2] + 1
i = 0
while i < len(x):
    print(i + 2, ' - ', x[i])
    i = i + 1

# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив
# со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если
# индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

from random import random
index = []
x = 10
array = [0] * x
for i in range(x):
    array[i] = int(random() * 10)
    if array[i] % 2 == 0:
        index.append(i)
print(array)
print(index)

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import random
x = 5
array = [0] * x
for i in range(x):
    array[i] = int(random() * 10)
print(array)


array[array.index(min(array))], array[array.index(max(array))] = array[array.index(max(array))], array[array.index(min(array))]

print(array)

# 4. Определить, какое число в массиве встречается чаще всего.

from random import random
x = 100
array = [0] * x
for i in range(x):
    array[i] = int(random() * 10)
print(array)

num = 0
max_count = 0
for i in range(x - 1):
    count = 1
    for j in range(i + 1, x):
        if array[i] == array[j]:
            count += 1
    if count > max_count:
        max_count = count
        num = array[i]

if max_count > 1:
    print(f'Число {num}, встретилось {max_count} раз(а)!')
else:
    print('bruh')

# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

from random import random
x = 10
array = [0] * x
for i in range(x):
    array[i] = int(random() * 10 - 1000)
print(array)

i = 0
index = 0
while i < x:
    if array[i] < 0 and index == -1:
        index = i
    elif array[i] < 0 and array[i] > array[index]:
        index = i
    i += 1

print(f'Число: {array[index]}, с индексом {index}')

# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import random
x = 5
array = [0] * x
for i in range(x):
    array[i] = int(random() * 10)
print(array)

min, max = 0, 0
for i in range(1, x):
    if array[i] < array[min]:
        min = i
    elif array[i] > array[max]:
        max = i
print(array[min], array[max])

if min > max:
    min, max = max, min

sum = 0
for i in range(min + 1, max):
    sum = sum + array[i]
print(f'Сумма чисел между наибольшими значениями: {sum}')

# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

from random import random

x = 5
array = [0] * x
for i in range(x):
    array[i] = int(random() * 10)
print(array)

min1 = 0
min2 = 1

for i in range(2, x):
    if array[i] < array[min1]:
        b = min1
        min1 = i
        if array[b] < array[min2]:
            min2 = b
    elif array[i] < array[min2]:
        min2 = i

print(f'Наименьшие числа: {array[min1], array[min2]}; с индексами: {min1, min2} соответственно.')

# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

x = 5
y = 4
z = []
for i in range(y):
    b = []
    sum = 0
    print(f'{i + 1} строка: ')
    for k in range(x - 1):
        n = int(input())
        sum = sum + n
        b.append(n)
    b.append(sum)
    z.append(b)

for i in z:
    print(i)

# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import random

x = 10
y = 5
z = []
for i in range(y):
    b = []
    for k in range(x):
        n = int(random() * 25)
        b.append(n)
        print('%4d' % n, end='')
    z.append(b)
    print()

max = -9999
for k in range(x):
    min = 9999
    for i in range(y):
        if z[i][k] < min:
            min = z[i][k]
    if min > max:
        max = min
print(f'Число {max} максимальное, среди минимальных.')
