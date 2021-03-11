'''CORES'''
redBold = '\033[1:31m'
yellowBold = '\033[1:33m'
greenBold = '\033[1:32m'
endColor = '\033[m'
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('Com a média {:.1f}, você foi {}REPROVADO{}.'.format(m, redBold, endColor))
elif m >= 5 and m < 7:
    print('Com a média {:.1f}, você ficou de {}RECUPERAÇÃO{}.'.format(m, yellowBold, endColor))
else:
    print('Com a média {:.1f}, você foi {}APROVADO{}!'.format(m, greenBold, endColor))
