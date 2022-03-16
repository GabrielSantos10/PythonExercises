"""a = float(input('Coloque o valor do cateto oposto: '))
b = float(input('Coloque o valor do cateto adjacente: '))
hip = (a**2 + b**2) ** (1/2)

print('A hipotenusa é {:.2f}' .format(hip))"""
from math import hypot

a = float(input('Coloque o valor do cateto oposto: '))
b = float(input('Coloque o valor do cateto adjacente: '))
hip = hypot()
print('A hipotenusa é {:.2f}'.format(hip))
