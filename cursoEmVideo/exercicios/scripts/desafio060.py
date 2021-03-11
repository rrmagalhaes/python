n = int(input('Digite um núemro para calcular o fatorial: '))
strfat = '{}! = '.format(n)
fat = n
while not n == 1:
    strfat += '{} X '.format(n)
    fat = fat * (n - 1)
    n += -1
strfat += '1 = {}'.format(fat)
print(strfat)
