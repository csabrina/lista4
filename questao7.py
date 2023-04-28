from calendar import isleap

ano = int(input("Digite o ano que deseja verificar se é bissexto:"))

if isleap(ano):
    print("{} é bissexto!" .format(ano))
else:
    print("{} não é bissexto!" .format(ano))