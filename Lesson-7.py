# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована
# в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

from random import randint

maximum = 100

def sort(z):
    for i in range(len(z) - 1, 0, -1):
        test = True
        for n in range(i):
            if z[n] > z[n+1]:
                z[n], z[n+1] = z[n+1], z[n]
                test = False

        if test == True:
            break
    return z

numbers = [randint(-100, 100) for _ in range(maximum)]
print(numbers)
print(sort(numbers))

# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

from random import randint

maximum = 50

def sort(z):
    if len(z) < 2:
        return z

    mid = len(z) // 2
    left_part = z[:mid]
    right_part = z[mid:]
    left_part = sort(left_part)
    right_part = sort(right_part)
    return m_list(left_part, right_part)

def m_list(list_1, list_2):
    result = []
    x = 0
    y = 0
    while x < len(list_1) and y < len(list_2):
        if list_1[x] <= list_2[y]:
            result.append(list_1[x])
            x += 1
        else:
            result.append(list_2[y])
            y += 1

    result += list_1[x:]
    result += list_2[y:]
    return result

numbers = [randint(0, 50) for _ in range(maximum)]

print(numbers)
print(sort(numbers))

# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках.

import random

def median_search(x, y, z):
    x = x.copy()
    inde = len(x) // 2

    if y >= z:
        return x[inde]

    pillar = x[inde]
    i = y
    j = z

    while i <= j:
        while x[i] < pillar:
            i += 1
        while x[j] > pillar:
            j -= 1
        if i <= j:
            x[i], x[j] = x[j], x[i]
            i += 1
            j -= 1

    if inde < i:
        x[inde] = median_search(x, y, j)
    elif j < inde:
        x[inde] = median_search(x, i, z)
    return x[inde]

m = random.randint(5, 10)
sum = 2 * m + 1
array = [random.randint(0, 50) for _ in range(sum)]
med = median_search(array, 0, len(array) - 1)

print(f'2*{m}+1 = {sum}  элементов:', array, sep='\n')
print(f'Медиана: {med}')
