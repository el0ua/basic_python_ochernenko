import math


def triangle_square_and_perimeter(a, b):
    s = (a * b) / 2
    p = math.sqrt(a**2 + b**2) + a + b
    return s, p


katet_1 = float(input('Введіть довжину першого катету трикутника: '))
katet_2 = float(input('Введіть довжину другого катету трикутника: '))

square, perimeter = triangle_square_and_perimeter(katet_1, katet_2)

print(f'Площа трикутника: {square:.2f}')
print(f'Периметр трикутника: {perimeter:.2f}')
