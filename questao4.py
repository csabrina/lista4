import math

saque = int(input("\nCédulas dispóniveis: R$ 50,00 e R$ 10,00\n\nDigite o valor que você gostaria de sacar:\n"))

if saque % 10 == 0:
    qntDe50 = math.ceil(saque//50)
    saque -= qntDe50*50

    qntDe10 = math.ceil(saque//10)
    saque -= qntDe10*10

    print("{} nota(s) de R$ 50,00\n{} nota(s) de R$ 10,00" .format(qntDe50, qntDe10))
else:
    print("\nValor está indisponivel para saque. Digite um valor de saque múltiplo de 10:")