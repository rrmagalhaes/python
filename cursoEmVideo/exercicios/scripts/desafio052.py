#Cores
red = '\033[31m'
yellow = '\033[33m'
notColor = '\033[m'
n = int(input('Digite um número inteiro: '))
cont = 0
for t in range(1, n + 1):
    if n % t == 0:
        print('{}{}{}'.format(yellow, t, notColor), end=' ')
        cont += 1
    else:
        print('{}{}{}'.format(red, t, notColor), end=' ')
if cont != 2:
    print('\nO número {} NÃO É PRIMO pois é divísivel por {} números!'.format(n, cont))
else:
    print('\nO número {} É PRIMO pois é divísivel apenas por 1 e por ele mesmo!'.format(n, cont))
