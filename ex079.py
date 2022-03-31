from os import system

lista = list()
system('cls')

while True:
    num = int(input('Insira um valor: '))
    if num not in lista:
        lista.append(num)
    else:
        print('Numero duplicado, nao adicionar...')
    p = str(input('Quer continuar?[S/N] ')).upper()
    while p not in 'SN':
        p = str(input('Quer continuar?[S/N] ')).upper()
    if p == 'N':
        break

print(sorted(lista))
