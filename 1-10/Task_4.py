"""
Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром,
полученное умножением двух двузначных чисел – 9009 = 91 × 99.

Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
"""


def find_palindrome():
    for i in range(999*999, 100*100-1, -1):
        s = str(i)
        if s == s[::-1]:
            for j in range(100, int(i**0.5)+1):
                if i % j == 0 and 99 < i // j < 1000:
                    return i
    return None


print(find_palindrome())



