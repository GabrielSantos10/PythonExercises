lista = list()

for c in range(0, 5):
    n = int(input('Digite um valor: '))
    pos1 = 0
    while pos1 < len(lista):
        if n == lista[pos1]:
            print('Esse valor ja existe. Não será inserido')
            break
        pos1 += 1
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Foi adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Foi adicionado à lista na posição {pos}')
                break        
            

print(f'Os valores digitados em ordem foram {lista}')
