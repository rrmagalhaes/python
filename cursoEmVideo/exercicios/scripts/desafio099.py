from time import sleep


def maior(* num):
    print('=' * 60)
    print('Analisando os valores passados:')
    for n in num:
        sleep(0.3)
        print(n, end=' ')
    print(f', foram informados {len(num)} valores ao todo!')
    if len(num) == 0:
        print()
    else:
        print(f'O maior valor informado foi {max(num)}')


# Progran
maior(5, 6, 8, 9, 15, -5, 1)
maior(-8, 10, 5)
maior(0)
maior()
