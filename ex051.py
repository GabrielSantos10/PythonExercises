a = int(input('Primeiro termo: '))
b = int(input('Razão: '))
d = a + (11 - 1) * b
for c in range(a, d, b):
    print(c, end='->')
print(' Acabou')
