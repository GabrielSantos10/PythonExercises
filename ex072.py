num = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')


while True:
    sel = int(input('Digite um numero de 0 a 20: '))
    if sel >= 0 and sel <= 20:
        break

print(num[sel])
