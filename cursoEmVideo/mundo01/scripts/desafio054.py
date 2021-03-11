from datetime import date
dAtual = date.today().year
maiores = 0
menores = 0
for n in range(0, 7):
    p = int(input('Digite o ano de nascimento: '))
    idade = dAtual - p
    if idade >= 18:
        maiores += 1
    elif idade < 18:
        menores += 1
print('{} pessoas não atingiram a maioridade e {} já são maiores!'.format(menores, maiores))
