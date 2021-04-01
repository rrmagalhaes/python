time = []
jogador = {}
cod = 1
while True:
    jogador.clear()
    gols = []
    jogador['codigo'] = cod
    jogador['nome'] = str(input('Nome do jogador: '))
    numjogos = int(input('Quantas partidas o jogador jogou? '))
    for g in range(1, numjogos + 1):
        ngol = int(input(f'Quantos gols na partida {g}? '))
        gols.append(ngol)
    jogador['gols'] = gols
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        escolha = str(input('Quer incluir outro jogador: [S/N] ')).upper()[0]
        if escolha in 'SN':
            break
    if escolha == 'N':
        break
    cod += 1
print("=" * 55)
print(f'{"Código":6}|{"Nome":^15}|{"Gols":^25}|{"Total":5}')
for p in time:
    print(f'{p["codigo"]:6}|{p["nome"]:>15}|{str(p["gols"]):>25}|{p["total"]:>5}')
qtcods = [999]
for i in time:
    qtcods.append(i['codigo'])
print(qtcods)
while True:
    while True:
        codEscolha = int(input('Digite o código para ver detalhes do jogador: (999 para sair) '))
        if codEscolha in qtcods:
            break
        else:
            print('Não existe jogador com esse código!')
    if codEscolha == 999:
        break
    print(f' -- LEVANTAMENTOS DO JOGADOR {time[codEscolha - 1]["nome"]}:')
    for k, v in enumerate(time[codEscolha - 1]['gols']):
        print(f'    => Na partida {k + 1}, fez {time[codEscolha - 1]["gols"][k]} gols.')
    print(f'{time[codEscolha - 1]["nome"]} fez {time[codEscolha - 1]["total"]} gols no total.')
print(' OBRIGADO POR UTILIZAR NOSSO PROGRAMA! ')
