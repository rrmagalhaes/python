listaProdutos = ('Arroz', 3.99, 'Feijão', 5.99, 'Biscoito', 1.99,
            'Leite 1L', 3.59, 'Leite Condensado', 3.19)
produtos = listaProdutos[0::2]
precos = listaProdutos[1::2]
soma = 0
cont = len(produtos)
print('{:-^50}'.format(' LISTA DE PRODUTOS '))
for p in range(0, cont):
    soma += precos[p]
    print('{:.<40} {}{:>7}'.format(produtos[p], 'R$', precos[p]))
print('{:.<40} {}{:>7}'.format('TOTAL', 'R$', soma))
print('-' * 50)