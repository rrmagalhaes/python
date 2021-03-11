velCarro = float(input('Qual a velocidade em que o carro esta? '))
if velCarro > 80:
    print('Você foi multado por excesso de velocidade!')
    valorMulta = (velCarro - 80) * 7
    print('O valor da multa é R$ {:.2f}'.format(valorMulta))
else:
    print('Parabéns, você esta no limite de velocidade!')
