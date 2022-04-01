lista0 = list()
lista1 = list()
lista2 = list()

while True:
    n = int(input('Insira um valor: '))
    lista0.append(n)
    r = str(input('Quer continuar?[S/N] ')).upper()
    while r not in 'SN':
        r = str(input('Quer continuar?[S/N] ')).upper()    
    if r == 'N':
        break

for c in lista0:
    if c % 2 == 0:
        lista1.append(c)
    else:
        lista2.append(c)

print(f'''lista completa {lista0}
lista só pares {lista1}
lista só impares {lista2}''')