matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para a posição [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^6}]', end='')
    print()

'''
matriz = [[], [], []]
q = n = 0
for q in range(0, 3):
    if q == 0:
        n = 1
        for n in range(1, 4):
            num = int(input(f"Digite um número para a posição [1, {n}]: "))
            matriz[0].append(num)
        n += 1
    elif q == 1:
        n = 1
        for n in range(1, 4):
            num = int(input(f"Digite um número para a posição [2, {n}]: "))
            matriz[1].append(num)
        n += 1
    elif q == 2:
        n = 1
        for n in range(1, 4):
            num = int(input(f"Digite um número para a posição [3, {n}]: "))
            matriz[2].append(num)
        n += 1
q += 1
print(matriz)
print('{:+^40}'.format(' Matriz 3x3 '))
print(f'1 - [{matriz[0][0]:^5}] [{matriz[0][1]:^5}] [{matriz[0][2]:^5}]')
print(f'2 - [{matriz[1][0]:^5}] [{matriz[1][1]:^5}] [{matriz[1][2]:^5}]')
print(f'3 - [{matriz[2][0]:^5}] [{matriz[2][1]:^5}] [{matriz[2][2]:^5}]')
'''