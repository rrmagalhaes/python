matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = soma3c = maior2l = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para a posição [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somapares += matriz[l][c]
print('=' * 50)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^6}]', end='')
    print()
print('=' * 50)
for m in range(0, 3):
    soma3c += matriz[m][2]
for m in range(0, 3):
    if m == 0:
        maior2l = matriz[1][m]
    else:
        if matriz[1][m] > maior2l:
            maior2l = matriz[1][m]
print(f'A soma de todos os pares é {somapares}.')
print(f'A soma dos valores da coluna 3 é {soma3c}.')
print(f'O maior valor da linha 2 é {maior2l}')
