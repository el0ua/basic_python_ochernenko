import math

def solve_quadratic_equation(a, b, c):
    d = b**2 - 4*a*c

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        return x1, x2
    elif d == 0:
        x = -b / (2*a)
        return x, None
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-d) / (2*a)
        return complex(real_part, imaginary_part), complex(real_part, -imaginary_part)


def main():
    a = float(input('Введіть значення a: '))
    b = float(input('Введіть значення b: '))
    c = float(input('Введіть значення с: '))

    x1, x2 = solve_quadratic_equation(a, b, c)

    if x1 is not None and x2 is not None:
        print(f'x1 = {x1}, x2 = {x2}')
    elif x1 is not None and x2 is None:
        print(f'x = {x1}')
    else:
        print(f'x1 = {x1}, x2 = {x2}')


def test():
    assert solve_quadratic_equation(1, -7, 12) == (4, 3)
    assert solve_quadratic_equation(1, 4, 4) == (-2, None)
    assert solve_quadratic_equation(1, 0, 1) == (complex(0, 1), complex(0, -1))


if __name__ == '__main__':
    main()
    test()
