p = list()
expressao = str(input('Digite a expressão: ')).strip().upper()
for c in expressao:
    if c == '(':
        p.append('(')
    elif c == ')':
        if len(p) > 0:
            p.pop()
        else:
            p.append(')')
            break
if len(p) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')


