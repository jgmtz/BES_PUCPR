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