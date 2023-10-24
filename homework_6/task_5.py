def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 ==0:
        return True
    else:
        return False


def main():
    year = int(input('Введіть рік: '))
    result = is_leap_year(year)

    if result is True:
        print('YES')
    else:
        print('NO')


def tests():
    assert is_leap_year(2024) is True
    assert is_leap_year(2023) is False


if __name__ == '__main__':
    main()
    tests()