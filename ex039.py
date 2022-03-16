dia = int(input('Qual dia você nasceu? '))
mes = int(input('Qual mês você nasceu? '))
ano = int(input('Qual ano você nasceu? '))
an = 2022 - ano
a = 18 - an
a1 = an - 18

if an <= 17:
    print('Falta {} anos para você se alistar.' .format(a))

elif an == 18:
    print('Está na hora de você se alistar.')

else:
    print('Passou do tempo de você se alistar há {} anos.' .format(a1))

print(an, ano, a, a1)
