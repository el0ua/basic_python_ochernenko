def sort_by_number_value(lst):
    return sorted(lst, key=lambda n: float(n))


def sort_by_first_digit(lst):
    return sorted(lst, key=lambda n: str(n)[0])


def main():
    original_list_1 = [5, '9', 0, '452', 6.5, '6', 1, 2]
    sorted_list_1 = sort_by_number_value(original_list_1)
    print(f'Список {original_list_1} відсортований за значенням числа елементу: {sorted_list_1}')

    original_list_2 = [472, 326, 1, 999.0, '1101000', '99', 9, '20', 863, '0']
    sorted_list_2 = sort_by_first_digit(original_list_2)
    print(f'Список {original_list_2} відсортований за значенням першої цифри числа: {sorted_list_2}')


if __name__ == '__main__':
    main()
