soma = 0
cont = 0
for n in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print('A soma dos {} números pares digitados é {}.'.format(cont, soma))




