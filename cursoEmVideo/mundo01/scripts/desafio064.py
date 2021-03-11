n = contn = soman = 0
n = int(input('Digite um número ou 999 para sair: '))
while n != 999:
    contn += 1
    soman += n
    n = int(input('Digite um número ou 999 para sair: '))
print('Foram digitados {} números!'.format(contn))
print('A soma de todos os números digitados é {}.'.format(soman))
