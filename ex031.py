n1 = float(input('Digite a distância em Km da viagem: '))
valor = n1*(1/2)
valor2 = n1 * 0.45

if n1 <= 200:
    print('O valor cobrado da viagem será {}!' .format(valor))
else:
    print('O valor cobrado da viagem será {}!' .format(valor2))
