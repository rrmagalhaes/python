def voto(ano):
    """
    Verifica se voto é obrigatório
    Desenvolvido por Renato Magalhães
    :param ano: recebe ano de nascimento
    :return: texto com idade e obrigatoriadade do voto
    """
    from datetime import date
    idade = date.today().year - ano
    if 16 <= idade < 18 or idade > 65:
        return f'Para pessoas com {idade} anos o voto é OPCIONAL'
    elif idade < 16:
        return f'Para pessoas com {idade} anos o voto é NEGADO'
    else:
        return f'Para pessoas com {idade} anos o voto é OBRIGATÓTIO'


# Program
ano = int(input('Ano de Nascimento: '))
print(voto(ano))
help(voto)
