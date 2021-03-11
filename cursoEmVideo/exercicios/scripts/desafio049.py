n = int(input('Digite o número que você quer a tabuada: '))
for t in range(1, 11):
    print('{} x {} = {}'.format(n, t, (n*t)))
