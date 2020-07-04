# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно
# вывести наименования предприятий, чья прибыль ниже среднего.

from collections import namedtuple

enterprise = namedtuple('enterprise', 'name q1 q2 q3 q4 full_year')
count_of_ent = int(input('Введите кол-во предприятий:  '))
ents = [0 for i in range(count_of_ent)]
full_sum = 0

for i in range(count_of_ent):
    full_year = 0
    name = input(f'Имя предприятия под номером {i + 1}: ')
    # quarters = [int(input('Введите прибыль в каждом квартале через пробел: ').split())]
    quarters = [int(k) for k in (input('Введите прибыль в каждом квартале через пробел: ').split())]
    for k in quarters:
        full_year += k
    full_sum += full_year
    ents[i] = enterprise(name, *quarters, full_year)

if count_of_ent > 1:
    average_sum = full_sum / count_of_ent
    if_less = []
    if_more = []

    for i in range(count_of_ent):
        if ents[i].full_year < average_sum:
            if_less.append(ents[i])
        else:
            if_more.append(ents[i])

    print(f'Средняя годовая прибыль: {average_sum}')
    print(f'Предприятия, чья прибыль меньше: ')
    for i in if_less:
        print(f'{i.name}, прибыль: {i.full_year}')
    print(f'Предприятия, чья прибыль больше: ')
    for i in if_more:
        print(f'{i.name}, прибыль: {i.full_year}')
else:
# print('bruh')
    print(f'{ents[0].name}, прибыль: {ents[0].full_year}')

# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число
# представляется как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import defaultdict
from collections import deque

values = '0123456789ABCDEF'
dict = defaultdict(int)
count = 0
for key in values:
    dict[key] = dict[key] + count
    count = count + 1

def value(bruh):
    x = 0
    num = deque(bruh)
    num.reverse()
    for i in range(len(num)):
        x = x + dict[num[i]] * 16 ** i
    return x

def action(bruh):
    x = deque()
    while bruh > 0:
        k = bruh % 16
        for i in dict:
            if dict[i] == k:
                x.append(i)
        bruh = bruh // 16
    x.reverse()
    return list(x)

num = input('Первое число: ').upper()
num2 = input('Второе число: ').upper()
number = value(num)
number2 = value(num2)
print(f'{num} + {num2}: {action(number + number2)}')
print(f'{num} * {num2}: {action(number * number2)}')
