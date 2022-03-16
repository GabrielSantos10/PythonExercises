preco = float(input('Digite o preço do produto: '))
d = float(input('Coloque o desconto: '))
print('o valor do produto com {}% de desconto é {:.2f}' .format(d, preco*((100-d)*0.01)))
