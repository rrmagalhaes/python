dados = list()
temp = list()
maior = menor = cont = 0
while True:
    escolha = ' '
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    dados.append(temp[:])
    if cont == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        elif temp[1] < menor:
            menor = temp[1]
    temp.clear()
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar [S/N]? ')).upper().strip()
        if escolha not in 'SN':
            print('Opção Inválida, digite S ou N!')
    if escolha == 'N':
        break
    cont += 1
#print(dados)
print(f'Foram cadastradas {len(dados)} pessoas.')
print(f'As pessoas com maior peso ({maior} Kg) são:', end=' ')
for p in dados:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'\nAs pessoas com menor peso ({menor} Kg) são:', end=' ')
for p in dados:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
