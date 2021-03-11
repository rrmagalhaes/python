somaidade = 0
cont = 0
contF = 0
idademaiorM = 0
nomeM= ''
print('=' * 50)
print('{:=^50}'.format(' ANALISADOR DE GRUPOS '))
print('=' * 50)
for p in range(1, 5):
    print('-' * 20, 'PESSOA {}'.format(p), '-' * 20)
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M ou F): ')).strip().upper()
    cont += 1
    somaidade += idade
    if sexo == 'M':
        if idade > idademaiorM:
            nomeM = nome
            idademaiorM = idade
    elif sexo == 'F':
        if idade < 20:
            contF += 1
print('A média de idade do grupo é \033[32m{:.0f}\033[m anos.'.format(somaidade/cont))
print('O homem mais velho é \033[31m{}\033[m com \033[32m{}\033[m anos.'.format(nomeM, idademaiorM))
print('No grupo tem \033[33m{}\033[m mulheres abaixo de 20 anos.'.format(contF))
print('=' * 50)
