def index(lst, elem):
    for i in range(len(lst)):
        if lst[i] == elem:
            return i
    return None


def main():
    lst = input('Введіть список елементів через кому: ').split(',')
    elem = input('Введіть елемент для прошуку: ')

    result = index(lst, elem)
    print(f'Індекс елемента {elem} в списку: {result}')


def tests():
    assert index([1, 2, 3, 4, 5], 3) == 2
    assert index([1, 2, 3, 4, 5], 7) is None
    assert index(['a', 'b', 'c', 'd'], 'b') == 1


if __name__ == '__main__':
    main()
    tests()