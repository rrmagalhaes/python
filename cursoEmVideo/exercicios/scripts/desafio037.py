print(('=' * 25), 'CONVERSOR DE NÚMEROS', ('=' * 25))
numero = int(input('Digite um número inteiro: '))
print('Que conversão você quer realizar?')
print('1 - BINÁRIO:')
print('2 - OCTAL:')
print('3 - para HEXADECIMAL.')
opcao = int(input('Digite a opção 1, 2 ou 3 para realizar a conversão: '))
print('=' * 85)
if opcao == 1:
    print('O número {} em binário é {}.'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('O número {} e octal é {}.'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('O número {} em hexadecimal é {}.'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida.')

