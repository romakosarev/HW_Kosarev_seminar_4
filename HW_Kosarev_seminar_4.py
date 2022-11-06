# 1. Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
from typing import List, Any

# n = float(input('введите дробное число: '))
# d = float(input('введите точность: '))
# str_d = str(d).split('.')
# print(round(n, len(str_d[1])))



# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# N =int(input("Введите число: "))
# for i in range(1, N):
#     if(N%i==0):
#         print(i)



# 3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

# a = list(map(int, input('Введите список чисел через пробел: ').split()))
# b = []
# [b.append(i) for i in a if i not in b]
# print(f'{b}')



# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

with open('p1.txt', 'w', encoding='utf-8') as file:
    file.write('1*x^2 + 2*x^3')
with open('p2.txt', 'w', encoding='utf-8') as file:
    file.write('4*x^5 + 6*x^7')
with open('p1.txt','r') as file:
    p1 = file.readline()
    list_p1 = p1.split()
with open('p2.txt','r') as file:
    p2 = file.readline()
    list_p2 = p2.split()
print(f'{list_p1} + {list_p2}')
sum_poly = list_p1 + list_p2
with open('sum_p.txt', 'w', encoding='utf-8') as file:
    file.write(f'{list_p1} + {list_p2}')
print('write to file!')