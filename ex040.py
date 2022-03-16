nota = float(input('Primeira nota: '))
nota1 = float(input('Segunda nota: '))
c = (nota + nota1) / 2
if c <= 5:
    print('REPROVADO')

elif c >= 7:
    print('APROVADO')

else:
    print('RECUPERAÇÃO')
