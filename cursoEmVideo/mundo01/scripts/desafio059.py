print('{:#^50}'.format(' Calculando Valores '))
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
opcao = 1
while opcao != 5:
    print('{:#^50}'.format(' Menu '))
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    print('#' * 50)
    opcao = int(input('Escolha sua opção: '))
    if opcao == 1:
        print('#' * 50)
        print('A soma de {} + {} é igual a {}.'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('#' * 50)
        print('A multiplicação de {} por {} é igual a {}.'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print('#' * 50)
            print('O maior número digitado é {}.'.format(n1))
        else:
            print('#' * 50)
            print('O maior número digitado é {}.'.format(n2))
    elif opcao == 4:
        print('#' * 50)
        n1 = int(input('Digite um novo número inteiro: '))
        n2 = int(input('Digite outro novo número inteiro: '))
    elif opcao == 5:
        print('Obrigado por usar nosso programa!')
        print('#' * 50)
        exit
    else:
        print('Opção inválida!')
