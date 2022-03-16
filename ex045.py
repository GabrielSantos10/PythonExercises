from random import randint
bot = randint(1, 3)
print('Regras: 1 é papel, 2 é tesoura e 3 é pedra')

p = int(input('insira um número: '))

if p == 1:
    j = 'papel'
elif p == 2:
    j = 'tesoura'
else:
    j = 'pedra'

if bot == 1:
    j1 = 'papel'
elif bot == 2:
    j1 = 'tesoura'
else:
    j1 = 'pedra'

if p == bot:
    print('Empate, os dois jogaram {}' .format(j))

elif p + 1 == bot:
    print('Você perdeu, o bot jogou {}' .format(j1))

elif bot < p:
    print('Você perdeu, o bot jogou {}' .format(j1))

elif bot + 1 == p:
    print('Você venceu')

else:
    print('Você venceu')
