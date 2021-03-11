s = 0
c = 0
for i in range(3, 501, 3):
    if i % 2 == 1:
        s = s + i
        c = c + 1
print('Soma dos {} números múltiplos de 3 entre 1 e 500 é \033[1:32m{}'.format(c, s))
