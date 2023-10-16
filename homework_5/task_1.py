import math


def degrees2radians(degrees):
    radians = degrees * math.pi / 180
    return radians


angle = [60, 45, 40]

radians_60 = degrees2radians(angle[0])
radians_45 = degrees2radians(angle[1])
radians_40 = degrees2radians(angle[2])

print(f'Значення cos {angle[0]} градусів: {math.cos(radians_60)}')
print(f'Значення cos {angle[1]} градусів: {math.cos(radians_45)}')
print(f'Значення cos {angle[2]} градусів: {math.cos(radians_40)}')
