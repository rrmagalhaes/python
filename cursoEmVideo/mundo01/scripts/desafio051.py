print('{:=^40}'.format(' 10 TERMOS DA PA '))
t = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
print('PA = (', t, end=' ')
for pa in range(1, 10):
    t = t + r
    print(t, end=' ')
print(')')

'''
décimo = t + (10 - 1) * r
for pa in range(t, décimo + r, r):
    print('{} ',.format(c), end=' ')
'''
