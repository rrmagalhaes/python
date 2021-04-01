def escreva(txt):
    tam = len(txt) + 2
    print('-' * tam)
    print(f' {txt}')
    print('-' * tam)


texto = str(input('Digite um texto qualquer: ')).strip()
escreva(texto)
