n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro néumro inteiro: '))
if n1 > n2:
    print('O primeiro número digitado, {}, é maior que o segundo número digitado, {}!'.format(n1, n2))
elif n1 < n2:
    print('O segundo número digitado, {}, é maior que o primeiro núemro digitado, {}!'.format(n2, n1))
else:
    print('Os números digitados são iguais!')