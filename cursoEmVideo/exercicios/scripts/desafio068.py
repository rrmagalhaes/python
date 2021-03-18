from random import randint
contVitoria = 0
while True:
    pc = randint(0, 10)
    jogador = int(input('Escolha o número: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Escolha PAR ou IMPAR [P/I]: ')).strip().upper()
    if escolha == 'P':
        escolha = 'PAR'
    else:
        escolha = 'IMPAR'
    soma = pc + jogador
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    if escolha == 'PAR' and resultado == 'PAR':
        print(f'O computador escolheu {pc} e você escolheu {jogador}')
        print(f'O resultado é {resultado}')
        print('VOCÊ VENCEU!')
        contVitoria += 1
    elif escolha == 'IMPAR' and resultado == 'IMPAR':
        print(f'O computador escolheu {pc} e você escolheu {jogador}')
        print(f'O resultado é {resultado}')
        print('VOCÊ VENCEU!')
        contVitoria += 1
    else:
        print(f'O computador escolheu {pc} e você escolheu {jogador}')
        print(f'O resultado é {resultado}')
        print('VOCÊ PERDEU!')
        print(f'Você acumulou {contVitoria} vitórias!')
        break



