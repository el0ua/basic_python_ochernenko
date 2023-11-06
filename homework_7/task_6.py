def fibonacci(n):
    if n < 1:
        return None
    elif n == 1:
        return 0
    else:
        a, b = 0, 1

        for _ in range(2, n):
            a, b = b, a + b
        return b


def main():
    n = int(input("Введіть позицію числа в послідовності Фібоначі: "))
    result = fibonacci(n)
    print(f'{n} число з послідовності Фібоначі: {result}')


def tests():
    assert fibonacci(1) == 0
    assert fibonacci(5) == 3
    assert fibonacci(10) == 34


if __name__ == '__main__':
    main()
    tests()