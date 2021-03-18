maior = menor = maiorp = menorp = 0
lista = list()
for n in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {n}: ')))
    if n == 0:
        maior = menor = lista[n]
    else:
        if lista[n] > maior:
            maior = lista[n]
        if lista[n] < menor:
            menor = lista[n]
print(f'Lista completa: {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for p, n in enumerate(lista):
    if n == maior:
        print(f'{p}... ', end='')
print(f'\nO menor valor digitado foi {menor} na posições ', end='')
for p, n in enumerate(lista):
    if n == menor:
        print(f'{p}... ', end='')
