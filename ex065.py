max = min = 0
x = 0
j = 0
y = 0
n = 0
while x == 0:
    n = int(input('Valor: '))
    j += n
    y += 1
    if y == 1:
        max = min = n
    else:
        if n > max:
            maior = n
        if n < min:
            min = n

    z = str(input('Quer cotinuar?[S/N] ').upper())
    if z == 'N':
        x = 1
print('Você inseriu {} numeros, o maior foi {} e o menor foi {}, e o total é {:.2f}' .format(y, max, min, j / y))
