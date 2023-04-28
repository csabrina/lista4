A = int(input("Digite o valor de A:\n"))

if A != 0:
    B = int(input("Digite o valor de B:\n"))
    C = int(input("Digite o valor de C:\n"))

    delta = (B**2) - 4 * A * C
    
    if delta < 0:
        print("A equação não possui raízes reais")
    elif delta == 0:
        x = ((-1)*(B)) / (2*A)
        print("A equação possui apenas uma raiz real:", x)
    else:
        x1 = (-B + delta ** (1 / 2)) / (2 * A)
        x2 = (-B - delta ** (1 / 2)) / (2 * A)
        print("x1: {} x2: {}" .format(x1,x2))

else:
    exit()



