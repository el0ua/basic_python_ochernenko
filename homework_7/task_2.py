def fizz_bizz(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return number


def main():
    for number in range(1, 101):
        result = fizz_bizz(number)
        print(result)


def tests():
    assert fizz_bizz(3) == 'Fizz'
    assert fizz_bizz(5) == 'Buzz'
    assert fizz_bizz(15) == 'FizzBuzz'
    assert fizz_bizz(7) == 7

if __name__ == '__main__':
    main()
    tests()
