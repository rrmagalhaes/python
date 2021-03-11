from random import randint
n = randint(0, 10)
contp = 0
p = int(-1)
while p != n:
    p = int(input('Tente adivinhar que número pensei: '))
    if p > n:
        print('Errrrou! O número é menor! Tente outra vez!')
    elif p < n:
        print('Errrrou! O número é maior! Tente outra vez!')
    contp += 1
print('Acertou! Você precisou de {} palpites para adivinhar!'.format(contp))
