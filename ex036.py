valorcasa = float(input('Qual o valor da casa? '))
salario = float(input('Qual seu salário? '))
anos = int(input('Em quantos anos você quer pagar? '))
meses = (anos * 12)
conta = valorcasa / meses
saldo = salario * 0.30

print(meses, conta, saldo)

if conta <= saldo:
    print('Você pode retirar o empréstimo')
else:
    print('Você não pode retirar o empréstimo')
