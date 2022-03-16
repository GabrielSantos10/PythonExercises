x = 0
a = 0
y = 0
while True:
    c = int(input('Valor: '))
    a += 1
    y += c
    if c == 999:
        break
print('O valor total é {} e você inseriu {} valores' .format(y - 999, a - 1))
