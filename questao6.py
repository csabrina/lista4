peso = float(input())
altura = float(input())

IMC = peso // (altura**2)

if IMC < 20:
    print("Abaixo do peso!")
elif 20 <= IMC <= 25:
    print("Normal!")
elif 25 < IMC <= 30:
    print("Excesso de peso!")
elif 30 < IMC <= 35:
    print("Obesidade!")
else: 
    print("Obesidade mórbida!")