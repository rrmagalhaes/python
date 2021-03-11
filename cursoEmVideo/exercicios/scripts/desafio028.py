from random import randint
from time import sleep
n = int(randint(0,5))
print('=' * 50)
print('Pensando...')
sleep(3)
print('=' * 50)
print('Pensei em um número de 0 a 5, que tal tentar adivinhar!')
print('=' * 50)
a = int(input('Digite qual você acha que foi: '))
print('=' * 50)
if n == a:
    print('Acertou miserávi, tu é ninja mesmo oh! Pensei mesmo no {}.'.format(a))
else:
    print('Não foi dessa vez projeto de guru! Pensei no {} e não no {}.'.format(n,a))