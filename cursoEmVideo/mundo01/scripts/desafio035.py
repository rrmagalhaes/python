l1 = float(input('Digite o primeiro cumprimento: '))
l2 = float(input('Diggite o segundo cumprimento: '))
l3 = float(input('Digite o terceiro cumprimento: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3< l1 + l2:
    print('Os valores {}, {} e {} podem formar um triângulo!'.format(l1, l2, l3))
else:
    print('Os valores {}, {} e {}  não podem formar um triângulo!'.format(l1, l2, l3))