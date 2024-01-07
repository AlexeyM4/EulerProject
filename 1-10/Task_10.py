"""
Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.

Найдите сумму всех простых чисел меньше двух миллионов.
"""


def is_simple(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_result():
    s = 2
    for i in range(3, 2_000_000, 2):
        if is_simple(i):
            s += i
    return s


print(get_result())


