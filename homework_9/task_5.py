def group_by_surname(list_of_enrollees):
    enrollees_number = {'A-I': 0, 'J-P': 0, 'Q-T': 0, 'U-Z': 0}

    for full_name in list_of_enrollees:
        surname_first_letter = full_name.split()[-1][0].upper()

        if surname_first_letter <= 'I':
            enrollees_number['A-I'] += 1
        elif surname_first_letter <= 'P':
            enrollees_number['J-P'] += 1
        elif surname_first_letter <= 'T':
            enrollees_number['Q-T'] += 1
        elif surname_first_letter <= 'Z':
            enrollees_number['U-Z'] += 1

    return enrollees_number


def main():
    list_of_enrolees = ['Buzz Aldrin', 'Noam Chomsky', 'Shirley Ann Jackson', 'Eric Sander', 'Marvin Zinsky']
    enrollees_number = group_by_surname(list_of_enrolees)

    for key, value in enrollees_number.items():
        print(f'{key}: {value}')


if __name__ == "__main__":
    main()
