import math

beta = float(input('Введіть число: '))

cos_beta = math.cos(beta)
sin_beta = math.sqrt(1 - cos_beta**2)
tan_beta = sin_beta / cos_beta
print(tan_beta)
