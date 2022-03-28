from os import system

system('cls')


palavras = ('mamaco','mocego','jaboti','camorça ,   jalecu','salmam','expinafre',)
for palavra in palavras:
    print(f'\nNa palavra {palavra} temos as vogais: ', end='')
    for leetra in palavra:
        if leetra.lower() in 'aeiou':
            print(leetra, end='')
