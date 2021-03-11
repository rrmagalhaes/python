preco = float(input('Digite o preço do produto para saber o valor com desconto: R$ '))
novoPreco = float(preco - preco * 0.05)
print('o preço com desconto de 5% fica: R$ {:.2f}'.format(novoPreco))
