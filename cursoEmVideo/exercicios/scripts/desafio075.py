contpar = 0
numeros = (int(input('Digite um número: ')), int(input('Digite um número: ')),
           int(input('Digite um número: ')), int(input('Digite um número: ')))
print('{:-^50}'.format(' NÚMEROS DIGITADOS '))
print(numeros)
print('{:-^50}'.format(' ANÁLISE '))
if 9 in numeros:
    print(f'O nove apareceu {numeros.count(9)} vezes!')
else:
    print('Não existe número \033[31m9\033[m na tupla!')
if 3 in numeros:
    print(f'O primeiro valor \033[33m3\033[m foi digitado na posição {numeros.index(3) + 1}.')
else:
    print(f'Não existe número \033[31m3\033[m na tupla!')
for p in range(0, 4):
    if numeros[p] % 2 == 0:
        contpar += 1
print(f'{contpar} números são pares.')
print('{:-^50}'.format(''))
