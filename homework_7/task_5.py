import random


def generate_random_number():
    return random.randint(1, 10)


def main():
    generated_number = generate_random_number()

    while True:
        user_guess = int(input('Вгадайте число від 1 до 10: '))

        if user_guess == generated_number:
            print('Ви вгадали число')
            break
        elif user_guess < generated_number:
            print('Ви не вгадали. Загадане число більше')
        else:
            print('Ви не вгадали. Загадане число менше')


if __name__ == '__main__':
    main()
