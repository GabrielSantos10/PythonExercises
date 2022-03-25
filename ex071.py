from os import system


system('cls')
num = int(input('Que valor você quer sacar? '))
ced = 50
totalced = 0
total = num
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'total de {totalced} cédulas foi de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0 
        if total == 0:
            break