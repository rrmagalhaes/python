nome = str(input('Digite um nome completo: ')).strip()
qtnomes = nome.count(' ')
nomes = nome.split()
print('O primeiro nome é {}.'.format(nomes[0]))
print('O último nome é {}.'.format(nomes[qtnomes]))

'''
print('O último nome é {}.'.format(nomes[len(nomes)-1]))
'''