peso = float(input('Quel é seu peso?(Kg) :'))
altura = float(input('Qual sua altura?(m) :'))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Seu IMC é de {:.1f}, e você esta ABAIXO DO PESO.'.format(imc))
elif imc <= 25:
    print('Seu IMC é de {:.1f}, e você esta no PESO IDEAL.'.format(imc))
elif imc <= 30:
    print('Seu IMC é de {:.1f}, e você esta em SOBREPESO.'.format(imc))
elif imc <= 40:
    print('Seu IMC é de {:.1f}, e você esta em OBESIDADE.'.format(imc))
else:
    print('Seu IMC é de {:.1f}, e você esta com OBESIDADE MORBIDA.'.format(imc))

