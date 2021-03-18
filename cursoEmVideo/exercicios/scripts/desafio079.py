listas = list()
while True:
    escolha = ' '
    numero = int(input('Digite um número: '))
    if numero not in listas:
        listas.append(numero)
        print(f'Número {numero} adicionado a lista!')
        print('-' * 50)
    else:
        print(f'Número {numero} já existe na lista e não foi adicionado!')
        print('-' * 50)
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar [S/N]? ')).strip().upper()
        print('-' * 50)
    if escolha == 'N':
        break
ordenados = list(sorted(listas))
print(f'Os números da lista são:', end=' ')
for p, n in enumerate(ordenados):
    print(f'{ordenados[p]}', end=' - ')
print('FIM')

