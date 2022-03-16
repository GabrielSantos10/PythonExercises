from math import sin, cos, tan, radians

angulo = float(input('Insira o angulo: '))
seno = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))

print('o angulo de {} tem o seno de {} \no angulo de {} tem o cosseno de {} \no angulo de {} tem a tangente de {}'
      .format(angulo, seno, angulo, cos, angulo, tan))
