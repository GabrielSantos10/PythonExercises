from os import system
import string


system('cls')
alunos = list()
aluno = list()
nota = list()
media = list()

while True:
    nome = str(input('Insira o nome do aluno: '))
    n1 = float(input('Insira a primeira nota do aluno: '))
    n2 = float(input('Insira a segunda nota do aluno: '))
    nota.append(n1)
    nota.append(n2)
    aluno.append(nome)
    aluno.append(nota[:])
    alunos.append(aluno[:])
    r = str(input('Quer continuar?[S/N]')).upper()
    while r not in 'SN':
        r = str(input('Quer continuar?[S/N]')).upper()
    if r == 'N':
        break
    aluno = list()
    nota = list()

for a in alunos[1]:
    for c in a:
        if  
        print(f'{c}')
