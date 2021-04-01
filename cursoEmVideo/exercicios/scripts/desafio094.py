from operator import itemgetter
lista = []
pessoa = {}
somaIdade = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    lista.append(pessoa.copy())
    while True:
        escolha = str(input('Deseja continuar o cadastro? [S/N] ')).upper()[0]
        if escolha in 'SN':
            break
        print('Digite apenas S ou N')
    if escolha == 'N':
        break
#print(lista)
print(f'Foram cadastradas {len(lista)} pessoas.')
temp = []
for p, n in enumerate(lista):
    temp.append(lista[p]['idade'])
media = sum(temp) / len(temp)
print(f'A média de idade das pessoas é {media:.1f} anos.')
print(f'As mulheres cadastradas foram : ', end=' ')
for p in lista:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}...', end=' ')
print(f'\nAs pessoas com idade acima da média são: ', end=' ')
for p in lista:
    if p['idade'] > media:
        print(f'{p["nome"]}...', end=' ')


