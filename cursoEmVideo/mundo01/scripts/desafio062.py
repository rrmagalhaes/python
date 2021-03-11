pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
termo = pt
cont = 1
contatermos = 0
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += r
    cont += 1
    contatermos += 1
print('FIM')
mtermos = 'S'
while mtermos not in '':
    mtermos = str(input('Você deseja mostrar mais termos? [S/N]: ')).strip().upper()
    if mtermos == 'S':
        qtermos = int(input('Mais quantos termos você quer mostrar? '))
        while qtermos >= 1:
            print('{} -> '.format(termo), end='')
            termo += r
            qtermos -= 1
            contatermos += 1
        print('PAUSA')
    elif mtermos == 'N':
        print('{} termos mostrados!'.format(contatermos))
        print('Obrigado por usar o programa!')
        exit()
    else:
        print('Opção Inválida, digite S ou N.')



