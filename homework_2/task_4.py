from decimal import Decimal


usd_cr = Decimal('37.45')
uah = Decimal(input('Введіть кількисть гривень: '))
usd = uah / usd_cr
print(f'Станом на 18 серпня 2023 року це становить {usd:.2f} Долларів США :(')