def sum_symbol_codes(first, last):
    total = 0

    for char_code in range(ord(first), ord(last)+1):
        total += char_code

    return total


def main():
    first = input('Введіть перший символ: ')
    last = input('Введіть останній символ: ')

    result = sum_symbol_codes(first, last)
    print(f'Сума Unicode кодів між символами {first} та {last} включно: {result}')


def tests():
    assert sum_symbol_codes('a', 'd') == 394
    assert sum_symbol_codes('1', '5') == 255


if __name__ == '__main__':
    main()
    tests()