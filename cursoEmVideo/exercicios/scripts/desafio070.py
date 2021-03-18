totGasto = prod1000 = menor = 0
cont = 0
while True:
    print('=' * 50)
    prod = str(input('Nome do produto: ')).strip().upper()
    preco = float(input('Preço do produto: R$  '))
    print('=' * 50)
    cont += 1
    totGasto += preco
    if preco > 1000:
        prod1000 += 1
    if cont == 1 or preco < menor:
        menor = preco
        maisBarato = prod
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Colocar outro produto na lista? [S/N]: ')).strip().upper()[0]
    if continua == 'N':
        break
print('{:=^50}'.format(' NOTINHA '))
print(f'O total gasto na compra foi R$ {totGasto:.2f}')
print(f'{prod1000} produtos custam mais que R$ 1000,00')
print(f'O produto mais barato foi o {maisBarato} custando R$ {menor}')
print('=' * 50)
