n = int(input('Quantos termos voce quer mostrar? '))
x = 0
t3 = 0
t1 = 0
t2 = 1
while x <= n:
    x += 1
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(t3, end='')
    print(' -> ', end='')
print('Fim')