num = int(input('Digite um número: '))
soma = maior = menor = num
contMedia = 1
decisao = str(input('Digitar outro número? [S/N]: ')).strip().upper()
if decisao in 'SN':
    while decisao == 'S':
        contMedia += 1
        num = int(input('Digite um número: '))
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
        soma += num
        decisao = str(input('Digitar outro número? [S/N]: ')).strip().upper()
        if decisao not in 'SN':
            print('Opção Inválida!')
else:
    print('Opção Inválida!')
media = (soma / contMedia)
print(soma)
print('Foram digitados {} números, a média entre eles é {}.'.format(contMedia, media))
print('O MAIOR valor digitado foi {} e o MENOR valor digitado foi {}.'.format(maior, menor))