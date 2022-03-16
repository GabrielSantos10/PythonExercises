n1 = int(input('Primeiro termo: '))
n2 = int(input('Razão da PA: '))
x = 0
c = 0
print(n1, end=' -> ')
while x == 0:
    n1 += n2
    c += 1
    print(n1, end=' -> ')

    if c == 10:
        x = 1
print('pausa')
v = int(input('Quantos você quer colocar a mais? '))
if v > 0:

    c = 0
    while x == 0:
        n1 += n2
        c += 1
        print(n1, end=' -> ')
        if c == v:
            x = 1
print('Fim')
