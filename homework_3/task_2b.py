# first try

number = int(input('Введіть трьохзначне ціле число: '))

if number >= 100 and number <= 999:
    d1 = number // 100
    d2 = (number - d1 * 100) // 10
    d3 = (number - d1 * 100 - d2 * 10)
    print (d1 + d2 + d3)
else:
    print('Введене значення не відповідає умовам')

# second try

number = int(input('Введіть трьохзначне ціле число: '))

if number >= 100 and number <= 999:
    d1 = number // 100
    d2 = (number // 10) % 10
    d3 = number % 10
    result = d1 + d2 + d3
    print (f'Сума усіх цифр трьохзначного цілого числа {number} є {result}')
else:
    print('Введене значення не відповідає умовам')

# third try

number = int(input('Введіть трьохзначне ціле число: '))

if  100 <= number <= 999:
    n1, d1 = divmod(number, 10)
    n2, d2 = divmod(n1, 10)
    result = n2 + d1 + d2
    print (f'Сума усіх цифр трьохзначного цілого числа {number} є {result}')
else:
    print('Введене значення не відповідає умовам')
