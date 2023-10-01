number = input('Введіть трьохзначне ціле число: ')

result = (ord(number[0]) - 48) + (ord(number[1]) - 48) + (ord(number[2]) - 48)
print (f'Сума усіх цифр трьохзначного числа {number} є {result}')