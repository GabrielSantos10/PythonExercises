dia = int(input('quantos dias você alugou o carro? '))
km = float(input('Quantos km você andou com o carro? '))
vdia = dia*60
vkm = km*0.15
vt = vdia + vkm

print('O total a pagar é {:.2f}' .format(vt))
