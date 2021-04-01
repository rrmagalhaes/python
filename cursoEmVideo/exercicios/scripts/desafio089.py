alunos = []
while True:
    escolha = ' '
    al = list()
    al.append(str(input('Aluno: ')).strip().upper())
    al.append(float(input("Nota 1: ")))
    al.append(float(input('Nota 2: ')))
    alunos.append(al)
    while escolha not in 'SN':
        escolha = str(input('Cadastrar novo aluno? [S/N] ')).strip().upper()
    if escolha == 'N':
        break
print(alunos)
print('{:|^40}'.format(' BOLETIM '))
for p, m in enumerate(alunos):
    print(f'{alunos[p][0]:.<37}{(alunos[p][1] + alunos[p][2])/2:.1f}')
print('{:|^40}'.format(''))
while True:
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja consultar as notas de algum aluno? [S/N] ')).strip().upper()
        if escolha == 'S':
            aluno = str(input('De qual aluno quer ver as notas? ')).strip().upper()
            for p, alu in enumerate(alunos):
                if aluno == alu[0]:
                    print(f'As notas do {aluno} foram {alunos[p][1]} e {alunos[p][2]}.')
    if escolha == 'N':
        print('OBRIGADO POR USAR NOSSO PROGRAMA!')
        break