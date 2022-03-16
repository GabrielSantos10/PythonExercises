prod = float(input('Digite o valor do produto: '))
pag = str(input('Meio de pagamento: '))
v1 = prod * 0.90
v2 = prod * 0.95
v3 = prod * 1.20
a = int

if pag == 'dinheiro' 'cheque':
    print('A pagar {:.2f}' .format(v1))

elif pag == 'cheque':
    print('A pagar {:.2f}' .format(v1))

elif pag == 'cartão':
    a = input('Quantas vezes? ')
    if a == 1:
        print('A pagar {:.2f}'.format(v2))
    else:
        print('A pagar {:.2f}' .format(v3))

else:
    print('Re-insira um valor')
