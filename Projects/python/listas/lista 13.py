'''Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto,
calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas
ocorreram (mostrar o mês por extenso: 1 - Janeiro, 2 - Fevereiro, . . . )'''
meses = [ "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temperaturas = []
for i in range(12):
    temp = float(input(f'digite a temperatura média do {i+1}° mes: '))
    temperaturas.append(temp)
media = sum(temperaturas)/len(temperaturas)
for i in range(12):
    if temperaturas[i] > media:
        print(f'{meses[i]} com media de {temperaturas[i]}°C')