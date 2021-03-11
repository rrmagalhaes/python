n = int(input('Quantidade de números a exibir da sequência de Fibonnaci: '))
print('=' * 50)
t1 = 0
t2 = 1
print('{} -> {} -> '.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('{} -> '.format(t3), end='')
    cont += 1
    t1 = t2
    t2 = t3
print('FIM')

'''n = int(input('Quantidade de números a exibir da sequência de Fibonnaci [Mínímo 3]: '))
if n >= 3:
    cont = n
    valor = 1
    valora = 0
    print('0, 1, ', end='')
    while cont > 2:
        if cont != 3:
            valor = valor + valora
            print('{}, '.format(valor), end='')
            valora = valor - valora
            cont -= 1
        else:
            valor = valor + valora
            print('{}'.format(valor), end='')
            valora = valor - valora
            cont -= 1
else:
    print('Opção inválida, programa encerrado!')
'''
