n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1 > n2 and n1 > n3 and n2 > n3:
    primeiro = n1
    segundo = n2
    terceiro = n3
else:
    if n1 > n2 and n1 < n3:
        primeiro = n3
        segundo = n1
        terceiro = n2
    else:
        if n1 < n2 and n1 > n3:
            primeiro = n2
            segundo = n1
            terceiro = n3
print('O número de maior valor é {} e o de menor valor é {}.'.format(primeiro, terceiro))

