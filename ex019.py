from random import choice

al1 = input('Primeiro aluno: ')
al2 = input('Segunod aluno: ')
al3 = input('Terceiro aluno: ')
al4 = input('Quarto aluno: ')
lista = [al1, al2, al3, al4]
escolhido = choice(lista)
print('O aluno escolhido é {}' .format(escolhido))