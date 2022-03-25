from os import system


system('cls')
prod = ''
pre = 0
continua = ''
total = 0
barato = 10000000
prodbara = ''
caro = 0

while True:
    prod = str(input('Insira o nome do produto: '))
    pre = int(input('Insira o valor do produto: '))
    continua = str(input('Quer continuar?[S/N] ')).upper()
    while continua not in 'S N':
        continua = str(input('Dado incorreto. Quer continuar?[S/N] ')).upper()
    total += pre 
    if pre < barato:
        barato = pre
        prodbara = prod
    if pre >= 1000:
        caro += 1   
    if continua == 'N':
        break

print(f'''O total gasto na compra foi R${total}.
{caro} produtos custam mais de 1000.
O produto mais barato foi {prodbara} que foi R${barato}.''') 
