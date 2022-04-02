from os import system
system('cls')

minimo = 1000
maximo = 0
lista = list()
pessoas = list()
num = list()
while True:
    nome = str(input('Digite o nome da pessoa: '))
    peso = float(input('Coloque o peso da pessoa: '))
    pessoas.append(nome)
    pessoas.append(peso)
    r = str(input('Quer continuar?[S/N]')).upper()
    lista.append(pessoas[:])
    while r not in 'SN':
       r = str(input('Quer continuar?[S/N]')).upper()
    if r == 'N':
        break
for c, v in enumerate(pessoas):
    if (c + 1) % 2 == 0:
        num.append(v)
for i in num:
    
    if i < minimo:
        minimo = i
    elif i > maximo:
        maximo = i
print(f'''Você inseriu {len(lista)} pessoas.
O peso máximo é {maximo}kg
O peso minimo é {minimo}kg''')
print(f'\n\n\n\npessoas{pessoas}, num{num}, lista{lista}')