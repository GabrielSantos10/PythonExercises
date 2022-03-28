from os import system


system('cls')
n = tuple(int(input('Insira um numero: '))for c in range(0, 5))
print(f'Você digitou os valores {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O valor 3 apareceu na posição {n.index(3) + 1}')
else:
    print(f'Não ha o valor 3')
print(f'Os valores pares digitados foram ', end='')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')