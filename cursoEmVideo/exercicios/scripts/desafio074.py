from random import randint
print('{:-^60}'.format(' SIMULADOR MEGA SENA '))
numeros = (randint(1, 60), randint(1, 60), randint(1, 60),
           randint(1, 60), randint(1, 60), randint(1, 60))
print('Os números sorteados foram:', end=' ')
for n in range(0, 6):
    print(f'{numeros[n]}', end=' ')
print('\n{:-^60}'.format(''))
print(f'O maior número é {max(numeros)}!')
print(f'O maior número é {min(numeros)}!')
print('-' * 60)
'''
nmaior = nmenor = 0
num = ' '
for n in range(0, 5):
    num += str(randint(0, 9))
    num += ' '
numeros = num.split()
for n in range(0, 5):
    if n == 0:
        nmaior = numeros[n]
        nmenor = numeros[n]
    else:
        if numeros[n] > nmaior:
            nmaior = numeros[n]
        if numeros[n] < nmenor:
            nmenor = numeros[n]
print('-' * 60)
print(f'Os números gerados foram {numeros[0:5]}')
print('-' * 60)
print(f'O maior número gerado foi {nmaior}.')
print(f'O menor número gerado foi {nmenor}.')
print('-' * 60)
'''