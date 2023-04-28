
data = input("Digite a data que deseja converter para extenso:\n").split('/')

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

dia = data[0]
mes = int(data[1])
mes= meses[mes - 1]
ano = int(data[2])

print(dia, "de", mes, "de", ano)

