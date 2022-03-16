v = float(input('Qual a velocidade em KM/h do carro? '))
multa = (v - 80)*7

if v >= 80:
    print('Voce foi multado em um montante de {}' .format(multa))
else:
    print('')
