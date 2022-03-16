num = int(input('Insira um valor: '))
print('''Escolha um dos três
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
p = int(input('Sua opção: '))

if p == 1:
    print('{} convertdo para BINÁRIO é igual a{}' .format(num, bin(num)[2:]))

elif p == 2:
    print('{} convertido para OCTAL é igual a {}' .format(num, oct(num)[2:]))
elif p == 3:
    print('{} convertido para HEXADECIMAL é igual a {}' .format(num, hex(num)[2:]))
else:
    print('Opção invalida. Tente novamente')
