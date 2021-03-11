frase = str(input('Digite uma frase: ')).strip().upper()
fsplit = frase.split()
fjoin = ''.join(fsplit)
#contrario = fjoin[::-1]
qt = len(fjoin)
contrario = ''
for l in range(qt - 1, -1, -1):
    contrario += fjoin[l]
print('O inverso de {} é {}.'.format(fjoin, contrario))
if fjoin == contrario:
    print('A frase digitada é um PALÍNDROMO!')
else:
    print('A frase digitada não é um PALÍNDROMO!')