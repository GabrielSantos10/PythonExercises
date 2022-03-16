import random
x = random.randint(1, 10)
c = 0
print('\33[34mFaremos um jogo, o computador escolhera um numero de 0 a 10, e você tentara acertar qual numero ele escolheu')
print('Que comece o jogo \n--------------------------\n\33[m')
a = int(input('Tente acertar o que o bot escolheu: '))

while a != x:
    a = int(input('\33[31mVocê errou tente novamente: '))
    c += 1

print('\33[34mVocê acertou o bot escolheu {}, você precisou de \33[37m{} \33[34mpara acertar' .format(x, c))