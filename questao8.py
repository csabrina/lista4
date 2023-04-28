
opcao = input("\nQual operação matemática você gostaria de realizar?\n\n[A] Soma\n[B] Subtração\n[C] Multiplicação\n[D] Divisão\n").upper()

if opcao =="A" or opcao =="B" or opcao =="C" or opcao =="D": 
    A = int(input("\nDigite o valor A:\n"))
    B = int(input("\nDigite o valor B:\n"))
    if opcao == "A":
        print("\nResultado =", A+B)
    elif opcao == "B":
        print("\nResultado =", A-B)
    elif opcao == "C":
        print("\nResultado =", A*B)
    else:
        print("\nResultado =", A//B)
else:
    print("Digite uma entrada válida")