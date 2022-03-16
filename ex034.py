salario = float(input('Qaul o salário do funcionário? '))
r1 = salario * 1.10
r2 = salario * 1.15
if salario >= 1250.00:
    print('O funcionario tera um aumento de 10%, e recebera {:.2f}!' .format(r1))
else:
    print('O funcionário tera um aumento de 15% e recebera {:.2f}!' .format(r2))
