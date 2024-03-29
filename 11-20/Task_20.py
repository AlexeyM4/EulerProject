"""
n! означает n × (n − 1) × ... × 3 × 2 × 1

Например, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
и сумма цифр в числе 10! равна 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Найдите сумму цифр в числе 100!.
"""

# from math import factorial
#
# print(sum(map(int, str(factorial(100)))))


def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact


print(sum(map(int, str(factorial(100)))))
