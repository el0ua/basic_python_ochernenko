from random import choice
from string import ascii_letters, digits


def generate_password(length):
    characters = ascii_letters + digits + "_"

    while True:
        password = "".join(choice(characters) for n in range(length))

        if (any(i.islower() for i in password) and
                any(i.isupper() for i in password) and
                any(i.isdigit() for i in password) and
                all(password[n] != password[n + 1] for n in range(len(password) - 1))):
            return password


def main():
    password_length = int(input("Введіть довжину паролю (мінімум 8 символів): "))
    password = generate_password(password_length)
    print(password)


if __name__ == "__main__":
    main()
