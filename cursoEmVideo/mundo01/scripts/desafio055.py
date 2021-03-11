pesomaior = 0
pesomenor = 0
for p in range(0, 5):
    peso = float(input('Digite o peso(Kg): '))
    if p == 0:
        pesomaior = peso
        pesomenor = peso
    else:
        if peso > pesomaior:
            pesomaior = peso

        if peso < pesomenor:
            pesomenor = peso

print('O maior peso digitado foi {} e o menor peso digitado foi {}!'.format(pesomaior, pesomenor))
