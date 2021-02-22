frase = str(input('Digite uma frase: ')).upper().strip()
print('O total de letras "a" na frase é {}'.format(frase.count('A')))
print('A primeira posição de "a" é {}.'.format(frase.find('A')+1))
print('A última posição de "a" é {}.'.format(frase.rfind('A')+1))