palavras = ('bola', 'suco', 'futebol', 'boxe',
            'samba', 'inconstitucional', 'riqueza',
            'pobreza', 'Palmeiras', 'Renato', 'Alvo')
for p in palavras:
    print(f'\nA palavra {p} tem as vogais ', end='')
    for letras in p:
        if letras in 'aAeEiIoOuU':
            print(f'\033[34m{letras}\033[m', end=' ')
