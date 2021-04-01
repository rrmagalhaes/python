numeros = [[], []]
valor = 0
for n in range(0, 7):
    valor = (int(input("Digite um número: ")))
    if valor % 2 == 0:
        numeros[0].append(valor)
    elif valor % 2 == 1:
        numeros[1].append(valor)
print(f'Valores pares -> {sorted(numeros[0])}')
print(f'Valores impares -> {sorted(numeros[1])}')


