x = int(input('Insira o valor que sera fatorado: '))
c = x
f = 1
print('Calculando {}! = ' .format(x), end='')
while c > 0:
    print('{}' .format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)
