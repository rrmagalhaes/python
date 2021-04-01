from random import randint
from time import sleep


def sorteia():
    print('Sorteando os 5 valores da lista:', end=' ')
    for n in range(0, 5):
        numeros.append(randint(0, 10))
    for n in numeros:
        sleep(0.3)
        print(f'{n}', end=' ')
    print('PRONTO!')


def somapar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {numeros}, temos {soma}.')


# Program
numeros = []
sorteia()
somapar(numeros)
