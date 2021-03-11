sexo = str(input('Digite o sexo: ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos, favor tente novamente: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))

