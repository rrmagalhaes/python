km = float(input('Quantos km você rodou com o carro? '))
dias = int(input('Por quantos dias você alugou o carro? '))
pKm = km * 0.15
pDias = dias * 60
pTotal = float(pKm + pDias)
print('O valor total a pagar é R$ {:.2f}, referente a R$ {:.2f} pelos {} Kms rodados e R$ {:.2f} pelos {} dias de aluguel.'.format(pTotal, pKm, km, pDias, dias))