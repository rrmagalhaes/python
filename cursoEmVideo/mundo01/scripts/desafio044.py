valor = float(input('Valor do produto: R$ '))
mPagamento = int(input('Escolha um método de pagamento:\n[1] DINHEIRO\n[2] CARTÃO\n-> '))
if mPagamento == 1:
    print('Para pagamentos à vista é concedido 10% de desconto, seu protudo sai de {:.2f} por: R$ {:.2f}!'.format(valor, valor * 0.9))
elif mPagamento == 2:
    tpagamento = int(input('Para pagamento no cartão escolha entre as opções:\n[1] À VISTA\n[2] PARCELADO\n-> '))
    if tpagamento == 1:
        print('Para pagamentos à vista no cartão é concedido 5% de desconto, seu produto sai de {:.2f} por: R$ {:.2f}!'.format(valor, valor * 0.95))
    elif tpagamento == 2:
        nparcelas = int(input('Em quantas parcelas você quer pagar? '))
        if nparcelas == 2:
            print('Para pagamentos parcelados em 2x no cartão é aplicado o valor normal, seu produto sai por: R$ {:.2f}!'.format(valor))
            print('O valor da parcela é R$ {}'.format(valor/nparcelas))
        else:
            print(
                'Para pagamentos parcelados em 3x ou mais no cartão é aplicado 20% de juros, seu produto sai de {:.2f} por R$ {:.2f}!'.format(
                    valor, valor * 1.2))
            print('O valor da parcela é R$ {}'.format((valor * 1.2)/nparcelas))
    else:
        print('Tipo de pagametno inválido!')
else:
    print('Método de pagamento inválido!')