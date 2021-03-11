print(('=' * 25), 'PEDIDO DE APROVAÇÃO DE EMPRÉSTIMO', ('=' * 25))
valorImovel = float(input('Qual o valor do imóvel? R$ '))
salario = float(input('Qual seu salário? R$ '))
anosPagamento = int(input('Em quantos anos pretende pagar? '))
print('=' * 85)
meses = anosPagamento * 12
parcela = float(valorImovel / meses)
if parcela > (salario * 0.30):
    print('Empréstimo NEGADO, a parcela de R$ {:.2f} fica acima de 30% do seu salário!'.format(parcela))
    print('=' * 85)
else:
    print('Empréstimo APROVADO com valor da parcela de R$ {:.2f} para pagamento em {} meses!'.format(parcela, meses))
    print('=' * 85)

