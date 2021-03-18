cont = soma = 0
while True:
    n = int(input('Digite um número inteiro [999 para sair]: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Foram digitados {cont} números e a soma entre eles é {soma}')
