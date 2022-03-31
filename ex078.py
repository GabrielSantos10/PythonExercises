from os import system



system('cls')
lista = [int(input('Insira um valor: ')), int(input('Insira um valor: ')), int(input('Insira um valor: ')),
         int(input('Insira um valor: ')), int(input('Insira um valor: '))]

maxi = max(lista)
mini = min(lista)

print(f'''O maior numero inserido foi {maxi} e ele está na posição {lista.index(max(lista))}.''')
for i, v in enumerate(lista):
    if v == max:
        print(f'{i}...', end='')
print()
print(f'''O menor numero inserido foi {mini} e ele está na posição {lista.index(min(lista))}''')
for i, v in enumerate(lista):
    if v == max:
        print(f'{i}...', end='')