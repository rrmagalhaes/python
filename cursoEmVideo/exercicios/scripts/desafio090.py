aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))
if aluno['media'] >= 6:
    aluno['situacao'] = '\033[32maprovado\033[m'
else:
    aluno['situacao'] = '\033[31mreprovado\033[m'
'''print(f'{aluno["nome"]} teve a média {aluno["media"]} e foi {aluno["situacao"]}!')'''
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
