v1 = int(input('Insira um valor: '))
v2 = int(input('Insira um valor: '))

while v1 != 1892839823:
    print('''\33[32m--Escolha o que fara com os dois valores inseridos--
\33[33m[1]somar
[2]multiplicar
[3]maior
[4]novos numeros
[5]sair do programa''')
    x = int(input('\33[35mQual numero?\33[36m '))
    if x == 1:
        print('{} + {} = {}' .format(v1, v2, (v1+v2)))
    elif x == 4:
        v1 = int(input('Insira um valor: '))
        v2 = int(input('Insira um valor: '))
    elif x == 2:
        print('{} * {} = {}' .format(v1, v2, (v1*v2)))
    elif x == 3:
        t = max(v1, v2)
        print('o maior é {}'.format(t))

    elif x == 5:

        v1 = 1892839823
print('\33[32mFim do programa')
