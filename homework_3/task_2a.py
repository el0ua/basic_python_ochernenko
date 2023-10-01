number = input('Введіть трьохзначне ціле число: ')

if len(number) == 3 and number.isdigit():
    print(int(number[0]) + int(number[1]) + int(number[2]))
else:
    print('Введене значення не відповідає умовам')

