modelos = ["Fusca", "Gol", "Uno", "Vectra", "Peugeout"]
consumo_por_litro = [7, 10, 12.5, 9, 14.5]
indice_carro_mais_economico = consumo_por_litro.index(max(consumo_por_litro))
print("Comparativo de Consumo de Combustível")
for i in range(len(modelos)):
    print(f"Veículo {i + 1}")
    print(f"Nome: {modelos[i]}")
    print(f"Km por litro: {consumo_por_litro[i]}")
preco_gasolina = 2.25
print("\nRelatório Final")
for i in range(len(modelos)):
    litros_necessarios = 1000 / consumo_por_litro[i]
    custo = litros_necessarios * preco_gasolina
    print(f"{i + 1} - {modelos[i]} - {consumo_por_litro[i]} - {litros_necessarios:.1f} litros - R$ {custo:.2f}")
print(f"\nO menor consumo é do {modelos[indice_carro_mais_economico]}")
