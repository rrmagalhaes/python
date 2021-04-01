from random import randint
from time import sleep
from operator import itemgetter
results = {}
ranking = []
print(f'{" Sorteando no dado! ":=^40}')
for j in range(1, 5):
    results[f'jogador{j}'] = randint(1, 6)
for k, v in results.items():
    sleep(1)
    print(f'O {k} tirou {v} no dado.')
ranking = sorted(results.items(), key=itemgetter(1), reverse=True)
print(ranking)
print(f'{" Vencedores ":=^40}')
for v, r in enumerate(ranking):
    sleep(1)
    print(f'O {v + 1}º lugar é {r[0]} que tirou {r[1]}')
