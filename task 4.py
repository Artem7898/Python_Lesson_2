"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
# 4 Решения:

def recursion(i, n1, n2, n3):
    if i ==n2:
        print(f"Количество элементов  - {n2}, их сумма - {n3} ")
    elif i < n2:
        return recursion(i + 1, n1 / 2 * - 1, n2, n3 + n1)

try:
    n2 = int(input("Введите количества элементов:"))
    recursion(0, 1, n2, 0)
except ValueError:
    print("Это строка не число!")