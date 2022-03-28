from os import system
from random import randint


system('cls')
a = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
for n in a:
    print(n, end=' ')
print(f'\nO maior foi {max(a)}, e o menor foi {min(a)}')
