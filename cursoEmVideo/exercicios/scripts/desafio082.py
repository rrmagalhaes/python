listaTodos = list()
listaPar = list()
listaImpar = list()
pos = 0
while True:
    escolha = ' '
    listaTodos.append(int(input('Digite um número: ')))
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar [S/N]: ')).strip().upper()
    if escolha == 'N':
        break
while pos <= (len(listaTodos) - 1):
    if listaTodos[pos] % 2 == 0:
        listaPar.append(listaTodos[pos])
    elif listaTodos[pos] % 2 == 1:
        listaImpar.append(listaTodos[pos])
    pos += 1
print('{:-^40}'.format(' Analise '))
print(f'Lista com todos os valores digitados: {listaTodos}')
print(f'Lista com números pares: {listaPar}')
print(f'Lista com números impares: {listaImpar}')