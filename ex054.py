for c in range(1, 7, 1):
    idade = int(input('Em que ano a {}° pessoa nasceu? ' .format(c)))

idcont = 2022 - idade
cont = 0
cont1 = 0
if idcont >= 18:
    cont += 1
else:
    cont1 += 1

if cont >= 1:
    print('Ao todo tivemos {} maiores de idade' .format(cont))
elif cont1 >= 1:
    print('Temos {} menores de idade' .format(cont1))
else:
    print('Ninguem nasceu ainda...')