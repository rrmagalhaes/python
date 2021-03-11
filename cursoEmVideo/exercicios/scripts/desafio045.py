from random import randint
from time import sleep
print('=' * 40)
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print(''' ESCOLHA SUA OPÇÃO
[ 0 ] - PEDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA
''')
jogador = int(input('Qual sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ !!!')
if jogador == 0 or jogador == 1 or jogador == 2:
    print('=' * 40)
    print('O computador escolheu {}'.format(itens[computador]))
    print('O jogador escolheu {}'.format(itens[jogador]))
    print('=' * 40)
    if computador == 0:
        if jogador == 0:
            print('DEU EMPATE')
        elif jogador == 1:
            print('VOCÊ VENCEU')
        elif jogador == 2:
            print('COMPUTADOR VENCEU!')
    elif computador == 1:
        if jogador == 0:
            print('COMPUTADOR VENCEU!')
        elif jogador == 1:
            print('DEU EMPATE')
        elif jogador == 2:
            print('VOCÊ VENCEU')
    elif computador == 2:
        if jogador == 0:
            print('VOCÊ VENCEU')
        elif jogador == 1:
            print('COMPUTADOR VENCEU!')
        elif jogador == 2:
            print('DEU EMPATE')
else:
    print('Jogada inválida!')
print('=' * 40)


'''
import random
import time
pc = random.randint(1, 3)
se = int(input( Escolha uma das opções: [1] - PEDRA | [2] - PAPEL | [3] - TESOURA -> ))
if pc == 1:
    escolha = str('PEDRA')
elif pc == 2:
    escolha = str('PAPEL')
elif pc == 3:
    escolha = str('TESOURA')

if se == 1:
    suaescolha = str('PEDRA')
elif se == 2:
    suaescolha = str('PAPEL')
elif se == 3:
    suaescolha = str('TESOURA')
else:
    print('Opção inválida, tente novamente.')
    exit()

print('Pedra...')
time.sleep(1)
print('Papel...')
time.sleep(1)
print('Tesoura...')
time.sleep(1)

print('{:=^40}'.format(' ESCOLHAS '))
print('Sua escolha: {}'.format(suaescolha))
print('Escolha do PC: {}'.format(escolha))
print('{:=^40}'.format(' RESULTADO '))
if (pc == 1 and se == 3) or (pc == 2 and se == 1) or (pc == 3 and se == 2):
    print('QUE PENA, VOCÊ PERDEU!')
elif pc == se:
    print('DEU EMPATE')
else:
    print('PARABÉNS, VOCÊ VENCEU!')
'''