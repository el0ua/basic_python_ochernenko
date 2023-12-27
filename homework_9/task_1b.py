import random


def diff_min_max(num_limit, lower_bound, upper_bound):
    random_numbers = [random.randint(lower_bound, upper_bound) for _ in range(num_limit)]
    random_numbers.sort()
    return random_numbers[num_limit - 1] - random_numbers[0]


def main():
    num_limit = int(input('Введіть кількість випадкових чисел: '))
    lower_bound = int(input('Введіть нижню границю діапазону: '))
    upper_bound = int(input('Введіть верхню границю діапазону: '))

    result = diff_min_max(num_limit, lower_bound, upper_bound)
    print(f'Різниця між максимальним та мінімальним значенням: {result}')


if __name__ == '__main__':
    main()