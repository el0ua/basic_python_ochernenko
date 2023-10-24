def is_even(number):
    return number % 2 == 0


def main():
    number = int(input('Введіть число: '))

    if is_even(number):
        print(f'Ведене число {number} є парним')
    else:
        print(f'Введене число {number} не є парним')


def test_is_even():
    assert is_even(1) is False
    assert is_even(2) is True
    assert is_even(-4) is True
    assert is_even(7.1) is False
    

if __name__ == '__main__':
    main()
    test_is_even()

