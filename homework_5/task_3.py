import math


def cone_square_and_volume(radius, height):
    l = math.sqrt(radius**2 + height**2)
    s = math.pi * radius * (l + radius)
    v = math.pi * radius**2 * height / 3
    return s, v


radius = float(input('Введіть радіус конуса: '))
height = float(input('Введіть висоту конуса: '))

square, volume = cone_square_and_volume(radius, height)

print(f'Площа конуса: {square:.2f}')
print(f'Об\'єм конуса: {volume:.2f}')