soma = 0

for c in range(1, 7):
    a = int(input('Insira um valor: '))
    if a % 2 == 0:
        soma += a

print('a soma dos numeros PARES inseridos é {}' .format(soma))
