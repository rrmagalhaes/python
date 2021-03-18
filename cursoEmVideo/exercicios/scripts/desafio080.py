lista = list()
for n in range(0, 5):
    num = int(input('Digite um número: '))
    if n == 0 or num > lista[-1]:
        lista.append(num)
        print(f'Valor inserido no final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Valor inserido na posição {pos}')
                break
            pos += 1
print(lista)
