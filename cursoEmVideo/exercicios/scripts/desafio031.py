kmViagem = float(input('Qual a distância da viagem em km? '))
if kmViagem <= 200:
    print('Para viagens de até 200km o valor é R$ 0,50 por km!')
    print('O preço da sua passagem é R$ {:.2f}.'.format(kmViagem * 0.5))
else:
    print('Para viagens acima de 200km o valor é R$ 0,45 por km!')
    print('O proço da sua passagem é R$ {:.2f}.'.format(kmViagem * 0.45))

