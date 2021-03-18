contNum = 1
pos = 0
pos5 = ''
lista = list()
while True:
    print('-' * 50)
    lista.append(int(input('Digite um número: ')))
    print('-' * 50)
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar [S/N]: ')).strip().upper()
    if escolha == 'N':
        print('{:-^50}'.format(' ANÁLISE '))
        break
    contNum += 1
print(f'Foram digitados {contNum} números!')
print('-' * 50)
lista.sort(reverse=True)
print(f'Lista ordenada de forma decrescente:\n{lista}')
print('-' * 50)
if 5 in lista:
    print(f'O número 5 foi digitado na lista!')
    print('-' * 50)
else:
    print(f'O número 5 NÃO foi digitatado e não esta na lista.')
    print('-' * 50)

