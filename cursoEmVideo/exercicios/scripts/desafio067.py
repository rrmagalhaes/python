while True:
    print('=' * 80)
    n = int(input('Digite o número para ver sua tabuada (número negativo para sair): '))
    print('=' * 80)
    if n < 0:
        break
    for t in range(1, 11):
        print(f'{n} x {t} = {n*t}')
print('Programa finalizado!')
