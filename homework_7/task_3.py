def calculate_wheat_chess_position(kilograms):
    chess_column = 'abcdefgh'
    total_seeds = kilograms / 0.03584
    current_seeds = 1
    cell_number = 1

    while current_seeds < total_seeds:
        current_seeds *= 2
        cell_number += 1

    row = (cell_number - 1)//8 + 1
    column = (cell_number - 1)%8 + 1
    chess_position = chess_column[column - 1] + str(row)

    return chess_position


def main():
    kilograms = float(input('Введіть вагу зерна в кг: '))
    result = calculate_wheat_chess_position(kilograms)
    print(result)


def tests():
    assert calculate_wheat_chess_position(0.03584) == 'a1'
    assert calculate_wheat_chess_position(0.07168) == 'b1'


if __name__ == '__main__':
    main()
    tests()