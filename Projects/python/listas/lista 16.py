contadores = [0] * 10
while True:
    vendas_brutas = float(input("Digite as vendas brutas do vendedor (-1 para encerrar): "))
    if vendas_brutas == -1:
        break
    salario = 200 + (0.09 * vendas_brutas)
    faixa_salarial = int(salario / 100)
    if faixa_salarial >= 10:
        faixa_salarial = 9 
    contadores[faixa_salarial] += 1
for i, contador in enumerate(contadores):
    if i == 9:
        print(f"i. $1000 em diante: {contador} vendedores")
    else:
        print(f"{chr(97 + i)}. ${200 + i * 100} - ${299 + i * 100}: {contador} vendedores")