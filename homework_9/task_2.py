import random


def diff_odd_even(num_limit, lower_bound, upper_bound):
    random_numbers = [random.randint(lower_bound, upper_bound) for _ in range(num_limit)]
    even_sum = sum(num for num in random_numbers if num % 2 == 0)
    odd_sum = sum(num for num in random_numbers if num % 2 != 0)
    return even_sum - odd_sum


def main():
    num_limit = int(input('Введіть кількість випадкових чисел: '))
    lower_bound = int(input('Введіть нижню границю діапазону: '))
    upper_bound = int(input('Введіть верхню границю діапазону: '))

    result = diff_odd_even(num_limit, lower_bound, upper_bound)
    print(f'Різниця між сумою усіх парних та непарних чисел: {result}')


if __name__ == '__main__':
    main()