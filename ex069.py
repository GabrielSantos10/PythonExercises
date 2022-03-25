from os import system


system('cls')
idade = 0
sexo = ''
continuar = 'sS'
Mas = 0
Fem = 0
id = 0
resp = ''

while True:
    print('Qual a idade? ')
    idade = int(input())
    print('Qual sexo?[M/F] ')
    sexo = str(input()).upper()
    while sexo not in 'MF':
        sexo = str(input('Valor errado, insira novamente: ')).upper()[0]
    if sexo != 'F' and idade < 20:
        Fem += 1
    if sexo == 'M':
        Mas += 1
    if idade >= 18:
        id += 1
    resp = str(input('Quer continuar? [S/N]')).upper()
    while resp not in 'SN':
        resp = str(input('Valor errado, insira novamente: ')).upper()[0]
    if resp == 'N':
        break
print(f'''
Há {id} pessoas tem mais de 18 anos.
Há {Mas} homens cadastrados.
Há {Fem} mulheres com menos de 20 anos''')
