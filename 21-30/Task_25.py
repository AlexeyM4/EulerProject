"""
Последовательность Фибоначчи определяется рекурсивным правилом:

Fn = Fn−1 + Fn−2, где F1 = 1 и F2 = 1.
Таким образом, первые 12 членов последовательности равны:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
Двенадцатый член F12 - первый член последовательности, который содержит три цифры.

Каков порядковый номер первого члена последовательности Фибоначчи, содержащего 1000 цифр?
"""


f1, f2 = 1, 1
n = 2
while len(str(f2)) < 1000:
    f1, f2 = f2, f1 + f2
    n += 1
print(n)

