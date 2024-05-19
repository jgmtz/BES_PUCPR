anos_luz = {
    "pc": 0.31,
    "al": 1,
    "ae": 63241.09,
    "ml": 525960.23,
    "sl": 31557600
}
unidades = ["Parsec (pc)", "Ano-Luz (al)", "Unidade Astronômica (ae)", "Minuto-Luz (ml)", "Segundo-Luz (sl)"]
print("Lista de unidades de conversão:")
for i, unidade in enumerate(unidades, start=1):
    print(f"{i}. {unidade}")
valor = float(input("\nValor a ser convertido: "))
print("\nUnidades disponíveis para conversão:")
for i, unidade in enumerate(unidades, start=1):
    print(f"{i}. {unidade}")
origem_idx = int(input("Converter de (Digite o número correspondente à unidade): ")) - 1
origem_unidade = unidades[origem_idx].split()[0]
destino_idx = int(input("Converter para (Digite o número correspondente à unidade): ")) - 1
destino_unidade = unidades[destino_idx].split()[0]
valor_convertido = valor * anos_luz[origem_unidade] / anos_luz[destino_unidade]
print(f"\nConversão: {valor} {origem_unidade} = {valor_convertido} {destino_unidade}")
