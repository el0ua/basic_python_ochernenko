import random


def get_max_digit_with_string(number):
    return int(max(str(number)))


def get_max_digit_without_string(number):
    max_digit = 0

    while number > 0:
        digit = number % 10

        if digit > max_digit:
            max_digit = digit

        number = number // 10
    return max_digit


def main():
    number = random.randint(100000000000, 999999999999)

    max_digit_1 = get_max_digit_with_string(number)
    print(f'Найбільша цифра числа {number}, знайдена з використанням рядків: {max_digit_1}')

    max_digit_2 = get_max_digit_without_string(number)
    print(f'Найбільша цифра числа {number}, знайдена без використання рядків: {max_digit_2}')


def tests():
    assert get_max_digit_with_string(9876543210) == 9
    assert get_max_digit_without_string(9876543210) == 9


if __name__ == '__main__':
    main()
    tests()