nome = str(input('Digite seu nome: '))
"""a = nome.upper()
b = nome.lower()
c = nome.split()
d = ''.join(c)
e = len(d)
f = ' '
g = nome.split(f, 1)[0]
h = len(g)
print('Nome: ', nome, '\nNome MAIUSCULO:', a, '\nNome minusculo:', b, '\nNome contagem de letras:', e, '\nSeu nome é', g,'Contagem primeiro nome: ', h)"""
#exercicio feito pelo prof embaixo
a = nome.split()
print('nome ', nome)
print('mai', nome.upper())
print('min', nome.lower())
print('num total {}' .format(len(nome)-nome.count(' ')))
print('primeiro nome é {} e tem {}' .format(a[0], len(a[0])))
