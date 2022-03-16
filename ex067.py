while True:
    a = int(input('\nEscolha um numero: '))
    for c in range(1, 11):
        b = a * c
        print(a, 'x', c, '=', b, end=' |  ')
    if a < 0:
        break
print('Fim do Programa')
