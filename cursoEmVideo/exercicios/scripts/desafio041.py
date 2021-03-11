from datetime import date
ano = int(input('Ano de nascimento do atleta: '))
anoatual = int(date.today().year)
if ano <= anoatual:
    idade = anoatual - ano
    if idade > 25:
        print('A atleta tem {} anos e sua categoria é MASTER.'.format(idade))
    elif 25 >= idade > 19:
        print('A atleta tem {} anos e sua categoria é SÊNIOR.'.format(idade))
    elif 19 >= idade > 14:
        print('A atleta tem {} anos e sua categoria é JUNIOR.'.format(idade))
    elif 14 >= idade > 9:
        print('A atleta tem {} anos e sua categoria é INFANTIL.'.format(idade))
    else:
        print('A atleta tem {} anos e sua categoria é MIRIM.'.format(idade))
else:
    print('O atleta ainda não nasceu, rs.')

