city = str(input('Qual o nome da cidade? ')).strip()
mai = city.upper()
quebra = mai.split()
print('A cidade {} começa com SANTO? \n RESULTADO -> {}'.format(mai, 'SANTO' in quebra[0]))

'''
city = str(input('Qual o nome da cidade? ')).strip()
valida = city[:5].upper() == 'SANTO'
print(valida)
'''