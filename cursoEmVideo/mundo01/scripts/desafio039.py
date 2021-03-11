from datetime import date
sexo = str(input('Digite M para masculino ou F para feminino: ')).strip().upper()
if sexo == 'M':
    ano = int(input('Em que ano você nasceu? '))
    anoatual = int(date.today().year)
    result = (anoatual - ano)
    anoideal = ano + 18
    if result == 18:
        print('Você precisa se alistar esse ano! Procure as forças armadas!')
    elif result > 18:
        print('Você passou do prazo de alistamento {} ano(os), procure as forças armadas URGENTE!'.format(result - 18))
        print('Seu ano de alistamento foi {}.'.format(anoideal))
    else:
        print('Ainda falta {} ano(os) para você se alistar'.format(18 - result))
        print('Seu ano de alistamento será em {}.'.format(anoideal))
elif sexo == 'F':
    print('Você não é obrigada a se alistar.')
else:
    print('Opção inválida')
