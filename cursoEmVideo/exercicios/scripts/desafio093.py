jogador = {}
gols = []
jogador['nome'] = str(input('Nome do jogador: '))
numjogos = int(input('Quantas partidas o jogador jogou? '))
for g in range(1, numjogos + 1):
    ngol = int(input(f'Quantos com na partida {g}? '))
    gols.append(ngol)
jogador['gols'] = gols
jogador['total'] = sum(gols)
print(f'{"-="*40}')
print(jogador)
print(f'{"-="*40}')
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print(f'{"-=" * 40}')
print(f'O jogador {jogador["nome"]} jogou {numjogos} partidas.')
for p, g in enumerate(jogador['gols']):
    print(f'    => Na partida {p + 1}, fez {gols[p]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
