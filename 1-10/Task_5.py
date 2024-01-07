"""
2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.

Какое самое маленькое число делится нацело на все числа от 1 до 20?
"""

from functools import reduce


def get_prime_divisors(num):
    res = []
    d = 2
    while num >= d:
        if num % d == 0:
            res.append(d)
            num //= d
        else:
            d += 1
    return res


sn = []
for i in range(1, 20+1):
    prime_divisors = get_prime_divisors(i)
    for j in set(prime_divisors):
        r = prime_divisors.count(j) - sn.count(j)
        if r > 0:
            sn.append(j * r)

print(reduce(lambda x, y: x * y, sn))
