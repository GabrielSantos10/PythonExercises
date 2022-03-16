sex = str(input('Masculino ou feminino? [M/F]').upper())

while sex not in 'MmFf':
    sex = str(input('Esse valor nao existe, tente novamente: ').upper())
print('Entendi você é {}' .format(sex))
