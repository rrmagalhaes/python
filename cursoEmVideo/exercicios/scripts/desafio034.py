sal = float(input('Qula o valor do seu salário? R$ '))
if sal > 1250:
    print('Você receberá um aumento de 10% equivalente a R$ {:.2f}.'.format(sal * 0.1))
    print('Seu novo salario será R$ {:.2f}.'.format(sal * 1.1))
else:
    print('Você receberá um aumento de 15% equivalente a R$ {:.2f}.'.format(sal * 0.15))
    print('Seu novo salario será R$ {:.2f}.'.format(sal * 1.15))
