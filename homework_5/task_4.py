def my_sum(*elements, start=0):
    return sum(elements, start)


numbers = input('Введіть будь-яку кількість чисел через пробіл: ')
numbers_list = map(float, numbers.split())

result = my_sum(*numbers_list)

print(f'Сума введених чисел і start: {result}')