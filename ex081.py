lista = list()
num = 1
while True:
    n = int(input('Insira um valor: '))
    print('Insira -1 para sair')
    if n == -1:
        break
    lista.append(n)
for c in lista:
    if c == 5:
        num += 1
if num % 2 == 0:
    r = 'Foi inserido' 
else:
    r = 'Não foi inserido'
lista.sort(reverse=True)
print(f'''\n\nForam inseridos {len(lista) -1}
Lista em ordem decrescente {lista}
O numero 5 {r} a lista''')