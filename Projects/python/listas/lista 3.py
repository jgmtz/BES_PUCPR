'''
Criar um programa que lê as temperaturas médias de cada mês
do ano e as armazena em uma lista. Usar um outro vetor para
guardar e exibir, quando necessário, os nomes dos meses do ano.
Calcular a média anual de temperatura, e informar quais meses
ficaram acima desta média anual
'''
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
temps = []
result = []
for i in range(12):
    temp = float(input(f'insira a temperatura do {i+1}° mes: '))
    temps.append(temp)
print(temps)
media = sum(temps)/len(meses)
media_up = []

for i in range(1, 13):
    if temps[i] > media:
        media_up.append(meses[i])
        media_up.append(temps[i])
        print(f'em {meses[i]} a temp foi de {temps[i]}°C, estando acima da média')