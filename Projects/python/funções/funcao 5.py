def roubo(taxaImposto, custo):
    return custo * (1 + taxaImposto / 100)


taxa = int(input('Digite a taxa de imposto (em %): '))
custo_inicial = int(input('Digite o custo do item: '))

custo_final = roubo(taxa, custo_inicial)
print(f'O preço final é: {custo_final:.2f}')
