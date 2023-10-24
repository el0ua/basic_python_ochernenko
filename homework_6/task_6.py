def sign(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1


def main():
    x = float(input('Введіть число x: '))
    result = sign(x)
    print(f'sign({x})={result}')


def tests():
    assert sign(2) == 1
    assert sign(0) == 0
    assert sign(-2) == -1


if __name__ == '__main__':
    main()
    tests()
