from math import hypot
print('-' * 50)
co = float(input('Qual o valor do cateto oposto? '))
ca = float(input('Qual o valor do cateto adjacente? '))
hi = hypot(co, ca)
print('O valor da hipotenusa é {:.2f}'.format(hi))
print('-' * 50)