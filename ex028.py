from random import randint
bot = randint(0, 5)
n1 = int(input('Tente adivinhar que numero o computador escolheu de 0 a 5:  '))

if n1 == bot:
    print('Voce acertou! O bot escolheu {}' .format(bot))
else:
    print('Você errou o bot escolheu {}' .format(bot))
