situacoes = {"necessita da esfera": 0, "necessita de limpeza": 0, "necessita troca do cabo ou conector": 0, "quebrado ou inutilizado": 0}
print("Levantamento de Mouses")
quantidade_mouses = 0
while True:
    identificacao = int(input("Número de identificação do mouse (ou 0 para encerrar): "))
    if identificacao == 0:
        break
    situacao = int(input("Situação do mouse (1 - necessita da esfera, 2 - necessita de limpeza, 3 - necessita troca do cabo ou conector, 4 - quebrado ou inutilizado): "))
    if 1 <= situacao <= 4:
        situacao_texto = {
            1: "necessita da esfera",
            2: "necessita de limpeza",
            3: "necessita troca do cabo ou conector",
            4: "quebrado ou inutilizado"
        }[situacao]
        situacoes[situacao_texto] += 1
        quantidade_mouses += 1
    else:
        print("Situação inválida. Por favor, insira uma situação de 1 a 4.")
print("\nRelatório:")
print(f"Quantidade de mouses: {quantidade_mouses}")
print("Situação               Quantidade   Percentual")
for situacao, quantidade in situacoes.items():
    percentual = (quantidade / quantidade_mouses) * 100 if quantidade_mouses > 0 else 0
    print(f"{situacao:<24} {quantidade:<12} {percentual:.1f}%")
