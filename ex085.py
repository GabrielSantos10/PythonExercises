lista = [list(), list()] 
for c in range(0, 7):
    n = int(input(f'Digite o {c + 1}° valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)


print(f'Os valores pares inseridos foram: {sorted(lista[0])}')
print(f'Os valores impares inseridos foram: {sorted(lista[1])}')
