r1 = int(input('reta 1: '))
r2 = int(input('reta 2: '))
r3 = int(input('reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Formam um triangulo ', end='')
    if r1 == r2 == r3:
        print('equilátero')
    elif r1 != r3 != r3 != r1:
        print('escaleno')
    else:
        print('isósceles')
else:
    print('NAO FORMAM UM TRIANGULO')
