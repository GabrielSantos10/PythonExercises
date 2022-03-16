from random import randint

while True:
    j = int(input('Diga um valor: '))
    c = randint(0, 10)
    t = j + c
    tipo = ''
    v = 0
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar?[P/I] ')).strip().upper()[0]
    print(f'Você jogou {j}, e o computador {c}. O total é {t}')
    if tipo == 'P':
        if t % 2 == 0:
            print('Voce VENCEU')
            v += 1
        else:
            print('Voce PERDEU!')
            break
    elif tipo == 'I':
        if t % 2 == 1:
            print('Voce VENCEU')
            v += 1
        else:
            print('Voce PERDEU!')
            break
    print('Vamos continuar jogando...')
print('Fim de jogo, tu perdeu')
