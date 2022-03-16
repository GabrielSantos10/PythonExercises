salario = float(input('Digite o salário do funcionário: '))
a = float(input('Digite a porcentagem do aumento: '))
print('O aumento de {}% do salário do funcionário será {:.2f}' .format(a, salario*((100+a)*0.01)))
