extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
           'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
           'quatorze', 'quinze', 'desesseis', 'desessete', 'desoito', 'desenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num > 20 or num < 0: # Pode usar -> if 0 <= num <= 20
        print('Número inválido!')
    else:
        print(f'Você digitou o número \033[32m{extenso[num]}\033[m!')
        break