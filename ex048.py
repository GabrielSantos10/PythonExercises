v = 500
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma += c
print('O total de numeros divisiveis por 3 são {}. A soma de todos os valores solocitado é {}' .format(cont, soma))
