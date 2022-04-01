'''n = str(input('Insira a expressao:\n'))
c = n.count('(')
b = n.count(')')
if b == c:
    print('Sua expressão esta valida!')
else:
    print('Sua expressão não é valida!')'''
e = str(input('Insira a expressao:\n'))
pilha = list()
for let in e:
    if let == '(':
        pilha.append('(')
    elif let == ')':
        if len(pilha) > 0:
            pilha.pop
    else:
        pilha.append(')')

if pilha == 0:
    print('Sua expressão esta valida!')
else:
    print('Sua expressão não é valida!')