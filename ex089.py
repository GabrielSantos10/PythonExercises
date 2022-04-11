from os import system
'''

system('cls')
alunos = list()
aluno = list()
nota = list()

while True:
    nome = str(input('Insira o nome do aluno: '))
    n1 = float(input('Insira a primeira nota do aluno: '))
    n2 = float(input('Insira a segunda nota do aluno: '))
    nota.append(n1)
    nota.append(n2)
    aluno.append(nome)
    aluno.append(nota[:])
    alunos.append(aluno[:])
    media = (n1 + n2) / 2
    alunos.append([media])
    r = str(input('Quer continuar?[S/N]')).upper()
    while r not in 'SN':
        r = str(input('Quer continuar?[S/N]')).upper()
    if r == 'N':
        break
    aluno = list()
    nota = list()

for c, a in enumerate(alunos):
        print(c, a)
while True:
    esc = int(input(f'Mostrar notas de qual aluno? (999 interrompe): '))
    if esc == 999:
        break
    else:
        print(alunos[esc])
'''

system('cls')

nota = list()

while True:
    nome = str(input('Insira o nome do aluno: '))
    n1 = float(input('Insira a primeira nota do aluno: '))
    n2 = float(input('Insira a segunda nota do aluno: '))
    media = (n1 + n2) / 2
    nota.append([nome, [n1, n2], media])
    r = str(input('Quer continuar?[S/N] '))
    if r in 'Nn':
        break
print()
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(nota):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')

while True:
    esc = int(input(f'Mostrar notas de qual aluno? (999 interrompe): '))
    if esc == 999:
        break
    if esc <= len(nota) - 1:
        print(f'{nota[esc][0]}{nota[esc][1]}')
print(f'{"VOLTE SEMPRE":^15}')