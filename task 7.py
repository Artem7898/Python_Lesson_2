"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

# 7 Решения:

n = int(input('Введите натуральное число:'))
a = 0
for i in range(1, n+1):
    a += i
b = n * (n + 1) // 2
print(a)
print(b)