from datetime import date
anoAtual = date.today().year
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
nasc= int(input('Ano de nascimento: '))
pessoa['ídade'] = anoAtual - nasc
pessoa['ctps'] = int(input('Carteira de trabalho: '))
if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: R$ '))
    pessoa['aposentadoria'] = (35 + pessoa['contratacao']) - nasc
print(f'{" Resultado ":-^40}')
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
