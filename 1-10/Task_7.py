"""
Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-е простое число - 13.

Какое число является 10001-м простым числом?
"""


def is_simple(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


count = 1
n = 3
while True:
    if is_simple(n):
        count += 1
        if count == 10_001:
            break
    n += 2
print(n)
