from os import system 


system('cls')

listagem = ('caderno',20,
'caneta',5,
'mochila',100,
'36 cores',70,
'fuzil',3000,
'lapiseira',15,
'kit de régua',40)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>5.2f}')
