def area(lar, comp):
    area = lar * comp
    print(f'A área de um terreno {lar} X {comp} é de {area}m².')


# Program
print(f'{" Controle de Terrenos ":-^40}')
lar = float(input('Largura do terreno(m): '))
comp = float(input('Comprimento do terreno(m): '))
area(lar, comp)
