from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contando de {i} até {f} de {p} em {p}!')
    if i < f:
        cont = i
        while cont <= f:
            sleep(0.3)
            print(cont, end=' ')
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            sleep(0.3)
            print(cont, end=' ')
            cont -= p
        print('FIM')


# Program
print(f'{"*" * 40}')
contador(1, 10, 1)
print(f'\n{"*" * 40}')
contador(10, 0, 2)
print(f'\n{"*" * 40}')
while True:
    escolha = str(input('Deseja fazer uma contagem personalizada? [S/N]: ')).strip().upper()[0]
    if escolha in 'SN':
        break
if escolha == 'N':
    print('< VOLTE SEMPRE >')
else:
    print('Por favor digite os dados para a contagem!')
    i = int(input('A partir de: '))
    f = int(input('Até: '))
    p = int(input('Qt de passos: '))
    contador(i, f, p)
print('\n< VOLTE SEMPRE >')
