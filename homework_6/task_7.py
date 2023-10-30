def fib(x):
    if x < 1:
        return None
    elif x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


def main():
    result = fib(20)
    print(f'20-те число з послідовності Фібоначі: {result}')


def tests():
    assert fib(1) == 0
    assert fib(5) == 3
    assert fib(10) == 34


if __name__ == '__main__':
    main()
    tests()

