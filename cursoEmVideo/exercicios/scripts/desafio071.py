print('[','{:=^60}'.format(' CAIXA ELETRÔNICO '), ']')
saque = int(input('Digite o valor que você deseja sacar: R$ '))
print('[','{:=^60}'.format(' TOTAL DE NOTAS '), ']')
cedula = 50
totalced = 0
while True:
    if saque >= cedula:
        saque -= cedula
        totalced += 1
    else:
        print(f'O total de notas de {cedula} é {totalced}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalced = 0
        if saque == 0:
            break
print('[','=' * 60, ']')
'''
print('[','{:=^60}'.format(' CAIXA ELETRÔNICO '), ']')
saque = int(input('Digite o valor que você deseja sacar: R$ '))
while saque != 0:
    if saque // 50 != 0:
        nota50 = saque // 50
        saque = saque % 50
    else:
        nota50 = saque // 50
    if saque // 20 != 0:
        nota20 = saque // 20
        saque = saque % 20
    else:
        nota20 = saque // 20
    if saque // 10 != 0:
        nota10 = saque // 10
        saque = saque % 10
    else:
        nota10 = saque // 10
    if saque // 1 != 0:
        nota1 = saque // 1
        saque = saque % 1
    else:
        nota1 = saque // 1
print('[','{:=^60}'.format(' TOTAL DE NOTAS '), ']')
print(f'NOTAS DE 50: {nota50}')
print(f'NOTAS DE 20: {nota20}')
print(f'NOTAS DE 10: {nota10}')
print(f'NOTAS DE 1 : {nota1}')
print('[','=' * 60, ']')
'''

