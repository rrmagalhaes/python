from random import randint
from time import sleep
palpites = []
print('{:-^50}'.format(' PALPITES DA MEGA SENA '))
quantjogos = int(input("Quantos palpites você que obter? "))
for q in range(0, quantjogos):
    palpites.append(list())
    for p in range(0, 6):
        if p == 0:
            num = randint(1, 60)
            palpites[q].append(num)
        else:
            num = randint(1, 60)
            if num not in palpites[q]:
                palpites[q].append(num)
            else:
                while num in palpites[q]:
                    num = randint(1, 60)
                palpites[q].append(num)
print('{:-^50}'.format(' Gerando palpites... '))
sleep(2)
for pal in range(0, quantjogos):
    print(f'Palpite n⁰ {pal + 1}: {sorted(palpites[pal])}')
    sleep(1)
print('-' * 50)
