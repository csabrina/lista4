A = int(input())
B = int(input())
C = int(input())

media = (A + B + C) / 3

if media >= 7:
    print("Aluno aprovado!")
elif 4 <= media < 7:
    print("Aluno deve fazer prova final!")
else:
    print("Aluno reprovado!")