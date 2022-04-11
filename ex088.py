from random import randint
from os import system
from time import sleep


system('cls')

n = int(input('Quantos jogos você quer fazer? '))
sena = list()
jogo = list()
print(f'Sorteando {n} Jogos')
for i in range(0, n):
    for c in range(0, 6):
        l = randint(1, 60)
        if l in jogo:                
            l = randint(1, 60)
        sena.append(l)
    jogo.append(sena[:])
    sena = list()
    print(jogo[i])
    sleep(1)    
print('Boa Sorte')
