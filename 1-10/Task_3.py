"""
Простые делители числа 13195 - это 5, 7, 13 и 29.

Каков самый большой делитель числа 600851475143, являющийся простым числом?
"""


def is_simple(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


number = 600_851_475_143
mx = 0
for i in range(1, int(number**0.5) + 1):
    if number % i == 0:
        j = number // i
        if is_simple(j):
            mx = max(mx, j)
            break
        elif is_simple(i):
            mx = max(mx, i)
print(mx)





