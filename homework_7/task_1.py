def knight_move(start_position, end_position):
    x1 = ord(start_position[0])
    y1 = int(start_position[1])
    x2 = ord(end_position[0])
    y2 = int(end_position[1])

    distance_x = abs(x1 - x2)
    distance_y = abs(y1 - y2)

    return (distance_x == 1 and distance_y == 2) or (distance_x == 2 and distance_y == 1)


def main():
    start_position = input('Веедіть дані першої клітини: ')
    end_position = input('Введіть дані другої клітини: ')

    result = knight_move(start_position, end_position)

    if result is True:
        print('Yes')
    else:
        print('No')


def tests():
    assert knight_move('a1', 'b3') == True
    assert knight_move('d2', 'h4') == False


if __name__ == '__main__':
    main()
    tests()