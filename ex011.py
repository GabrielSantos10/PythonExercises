a = float(input('Digite a altura em metros da parede: '))
l = float(input('Digite a largura em metros da parede: '))
m = a*l
print('A parede tem {}m² e a quantidade de tinta necessária para pinta-la é {:.2f}L' .format(m, m/2))
