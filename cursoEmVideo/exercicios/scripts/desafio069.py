maiores = homens = mulheres = 0
while True:
    sexo = 'a'
    resposta = 'a'
    idade = int(input('Digite a idade: '))
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    if idade > 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        mulheres += 1
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar o cadastro? [S/N]: ')).strip().upper()
    if resposta == 'N':
        break
print(f'Foram cadastradas {maiores} pessoas com mais de 18 anos.')
print(f'{homens} homens foram cadastrados.')
print(f'{mulheres} mulheres com menos de 20 anos foram cadastradas.')