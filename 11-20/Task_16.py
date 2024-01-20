"""
2**15 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.

Какова сумма цифр числа 2**1000?
"""


def get_result(num):
    return sum(map(int, str(num)))


print(get_result(2**1000))



