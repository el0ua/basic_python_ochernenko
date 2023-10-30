def circles_intersect(x1, y1, r1, x2, y2, r2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5 <= (r1 + r2)


def main():
    x1 = float(input('Введіть координату x для першого кола: '))
    y1 = float(input('Введіть координату y для першого кола: '))
    r1 = float(input('Введіть радіус першого кола: '))
    x2 = float(input('Введіть координату x для другого кола: '))
    y2 = float(input('Введіть координату y для другого кола: '))
    r2 = float(input('Введіть радіус другого кола: '))

    result = circles_intersect(x1, y1, r1, x2, y2, r2)
    if result:
        print('Кола перетинаються')
    else:
        print('Кола не перетинаються')


def tests():
    assert circles_intersect(0, 0, 1, 2, 2, 2) == True
    assert circles_intersect(0, 0, 1, 4, 4, 1) == False


if __name__ == '__main__':
    main()
    tests()

