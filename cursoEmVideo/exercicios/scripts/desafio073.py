brasileiro = ('Palmeiras', 'Flamengo', 'Internacional', 'Gremio', 'São Paulo',
              'Atletico Mineiro', 'Atletico Paranaense', 'Cruzeiro', 'Botafogo',
              'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense',
              'Ceará', 'Vasco', 'Sport', 'America MG', 'Vitoria', 'Parana')
print('{:-^60}'.format(' 5 PRIMEIROS COLOCADOS '))
for c in range(0, 5):
    print(f'{c + 1}° colocado - {brasileiro[c]}')
print('{:-^60}'.format(' ULTIMOS 4 COLOCADOS '))
for c in range(16, 20):
    print(f'{c + 1}° colocado - {brasileiro[c]}')
print('{:-^60}'.format(' NOMES EM ORDEM ALFABETICA '))
alfa = (sorted(brasileiro))
for c in range(0, 20):
    print(f'{alfa[c]}')
print('{:-^60}'.format(' POSICAO DA CHAPECOENSE '))
print(f'A Chapecoense esta na {brasileiro.index("Chapecoense", 0) + 1}° posição!')
print('-' * 60)
