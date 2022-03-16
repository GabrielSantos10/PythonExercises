peso = float(input('Coloque seu peso: '))
altura = float(input('Coloque sua altura: '))
alt = altura * altura
imc = peso / alt

if imc <= 18.5:
    print('Abaixo do peso')

elif imc <= 25:
    print('Peso ideal')

elif imc <= 30:
    print('Sobrepeso')

elif imc <= 40:
    print('Obesidade')

else:
    print('Obesidade mórbida')

print('Seu imc é {:.1f}, abaixo de 18.5 é abaixo do ideal, abaixo de 25 ideal, 30 sobrepeso, 40 obeso, e acima de 40 morbido' .format(imc))
