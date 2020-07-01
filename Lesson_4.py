# 1. Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.

# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

# Взял из второго урока свой вариант
# x = int(input('Введите число: '))
# y = 0
# z = 1
# for i in range(x):
#     y = y + z
#     z = z / -2
# print(f'Ответ: {y}')

import cProfile, timeit

def bruh(x):
    y = 0
    z = 1
    for i in range(x):
        y = y + z
        z = z / -2
    return y

cProfile.run('bruh(10000)')

# py -m timeit -n 100 -s "import test" "test.bruh(10)"
# 100 loops, best of 5: 3.61 usec per loop

# py -m timeit -n 100 -s "import test" "test.bruh(100)"
# 100 loops, best of 5: 17.6 usec per loop

# py -m timeit -n 100 -s "import test" "test.bruh(1000)"
# 100 loops, best of 5: 88.7 usec per loop

# py -m timeit -n 100 -s "import test" "test.bruh(10000)"
# 100 loops, best of 5: 951 usec per loop

# при увеличении кол-во вводимых данных в 10 раз, скорость изменяется незначительно

# 4 function calls in 0.002 seconds
# ncalls tottime percall cumtime percall filename: lineno(function)
# 1 0.000 0.000 0.002 0.002 < string >: 1( < module >)
# 1 0.002 0.002 0.002 0.002 test2.py: 3(bruh)
# 1 0.000 0.000 0.002 0.002 {built - in method builtins.exec}
# 1 0.000 0.000 0.000 0.000 {method 'disable' of '_lsprof.Profiler' objects}

def bruh1(x):
    sum = 0
    for i in range(x):
        sum = sum + (-1) ** i / 2 ** i
    return sum

cProfile.run('bruh1(10000)')

# 4 function calls in 0.378 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.378    0.378 <string>:1(<module>)
#        1    0.378    0.378    0.378    0.378 test2.py:14(bruh1)
#        1    0.000    0.000    0.378    0.378 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# py -m timeit -n 100 -s "import test" "test.bruh1(10)"
# 100 loops, best of 5: 10.4 usec per loop
# py -m timeit -n 100 -s "import test" "test.bruh1(100)"
# 100 loops, best of 5: 169 usec per loop
# py -m timeit -n 100 -s "import test" "test.bruh1(1000)"
# 100 loops, best of 5: 2.17 msec per loop
# 10000 не дождался
# Алгоритм имеет линейную сложность, при увеличении входящих данных в 10 скорость сильно изменяется


NUMBER_EXECUTIONS = 1
test = 10000

time1 = timeit.timeit(f'bruh({test})', setup='from __main__ import bruh', number=NUMBER_EXECUTIONS)
time2 = timeit.timeit(f'bruh1({test})',
                      setup='from __main__ import bruh1',
                      number=NUMBER_EXECUTIONS)
print(f'{time1}')
print(f'{time2}')
print(f'{time2/time1}')
# Первоначальный способ оказался быстрее в 292 раза

# 2. Написать два алгоритма нахождения i-го по счёту простого числа.

import math, cProfile

def prime(i):
    number_of_primes = 0
    number = 2
    while number_of_primes <= i:
        number_of_primes = number / math.log(number)
        number += 1
    return number

def erato(i):
    i_max = prime(i)
    lst_prime = [_ for _ in range(2, i_max)]
    for number in lst_prime:
        if lst_prime.index(number) <= number - 1:
            for j in range(2, len(lst_prime)):
                if number * j in lst_prime[number:]:
                    lst_prime.remove(number * j)
        else:
            break
    return lst_prime[i - 1]

def without_erato(i):
    lst_prime = [2]
    number = 3
    while len(lst_prime) < i:
        flag = True
        for j in lst_prime.copy():
            if number % j == 0:
                flag = False
                break
        if flag:
            lst_prime.append(number)
        number += 1
    return lst_prime[-1]

cProfile.run('without_erato(1000)')
# Не используя решето
# ncalls tottime percall cumtime percall filename: lineno(function)
# 1 0.000 0.000 0.065 0.065 < string >: 1( < module >)
# 1 0.057 0.057 0.065 0.065 test.py: 23(without_erato)
# 1 0.000 0.000 0.065 0.065 {built - in method builtins.exec}
# 7918 0.001 0.000 0.001 0.000 {built - in method builtins.len}
# 999 0.000 0.000 0.000 0.000 {method 'append' of 'list' objects}
# 7917 0.007 0.000 0.007 0.000 {method 'copy' of 'list' objects}
# 1 0.000 0.000 0.000 0.000 {method 'disable' of '_lsprof.Profiler' objects}

#  16838 function calls in 0.065 seconds

# py -m timeit -n 100 -s "import test" "test.without_erato(10)"
# 100 loops, best of 5: 28.8 usec per loop
# py -m timeit -n 100 -s "import test" "test.without_erato(100)"
# 100 loops, best of 5: 551 usec per loop
# py -m timeit -n 100 -s "import test" "test.without_erato(500)"
# 100 loops, best of 5: 11.6 msec per loop
# Время выполнения нарастает. Рекурсий нет.

cProfile.run('erato(1000)')
# Используя решето
# ncalls tottime percall cumtime percall filename: lineno(function)
# 1 0.000 0.000 4.138 4.138 < string >: 1( < module >)
# 1 3.860 3.860 4.138 4.138 test.py: 11(erato)
# 1 0.001 0.001 0.001 0.001 test.py: 13( < listcomp >)
# 1 0.005 0.005 0.008 0.008 test.py: 3(prime)
# 1 0.000 0.000 4.139 4.139 {built - in method builtins.exec}
# 1130 0.000 0.0000.000 0.000 {built - in method builtins.len}
# 9118 0.003 0.000 0.003 0.000 {built - in method math.log}
# 1 0.000 0.000 0.000 0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 1130 0.010 0.000 0.010 0.000 {method 'index' of 'list' objects}
# 7988 0.259 0.000 0.259 0.000 {method 'remove' of 'list' objects}

#  19372 function calls in 4.139 seconds
# Суммарное время по сравнению с решетом ~ в 60 раз в пользу второго

# py -m timeit -n 100 -s "import test" "test.erato(10)"
# 100 loops, best of 5: 203 usec per loop
# py -m timeit -n 100 -s "import test" "test.erato(100)"
# 100 loops, best of 5: 10.9 msec per loop
# py -m timeit -n 100 -s "import test2" "test2.erato(500)"
# 100 loops, best of 5: 602 msec per loop
# С увеличением объема входных данных время выолнения увеличивается катастрофически.


# Вывод: Алгоритм с использованием решета гораздо эффективнее.
