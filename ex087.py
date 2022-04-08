from os import system


system('cls')
'''
matriz = list()
linha1 = list()
linha2 = list()
linha3 = list()
contador1 = [0, 0, 0]
contador2 = [1, 1, 1]
contador3 = [2, 2, 2]
while True:
    for c, v in enumerate(contador1):
        linha1.append(int(input(f'Digite um valor para [{v, c}]: ')))
    for c, v in enumerate(contador2):
        linha2.append(int(input(f'Digite um valor para [{v, c}]: ')))
    for c, v in enumerate(contador3):
        linha3.append(int(input(f'Digite um valor para [{v, c}]: ')))
    break
matriz.append(linha1)
matriz.append(linha2)
matriz.append (linha3)
print(f'[{matriz[0][0]}] [{matriz[0][1]}] [{matriz[0][2]}]
[{matriz[1][0]}] [{matriz[1][1]}] [{matriz[1][2]}]
[{matriz[2][0]}] [{matriz[2][1]}] [{matriz[2][2]}]')'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para {l}, {c}: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'{matriz[l][c]:^5}', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
print()
print(f'A soma dos valores em paré {spar}.')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma da terceira coluna é {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}.')
