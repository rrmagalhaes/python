l1 = float(input('Digite o primeiro cumprimeto: '))
l2 = float(input('Digite o segundo cumprimento: '))
l3 = float(input('Digite o terceiro cumprimento: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os cumprimentos {}, {}, {} formam um triângulo '.format(l1, l2, l3), end='')
    if l1 == l2 and l1 == l3:
        print('EQUIlÁTERO!')
    elif l1 != l2 and l2 != l3 and l1 != l3:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')

else:
    print('Os cumprimentos {}, {}, {} NÃO formam um triângulo.'.format(l1, l2, l3))
