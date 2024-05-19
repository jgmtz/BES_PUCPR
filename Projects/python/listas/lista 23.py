def bytes_para_mb(bytes):
    return bytes / (1024 * 1024)
def calcular_percentual(espaco, total):
    return (espaco / total) * 100
with open("usuarios.txt", "r") as arquivo:
    linhas = arquivo.readlines()
espaco_total = 0
usuarios = []
for linha in linhas:
    nome, espaco = linha.split()
    espaco = int(espaco)
    espaco_total += espaco
    usuarios.append((nome, espaco))
usuarios.sort(key=lambda x: x[1], reverse=True)
with open("relatório.txt", "w") as relatorio:
    relatorio.write("ACME Inc. Uso do espaço em disco pelos usuários\n")
    relatorio.write("-" * 60 + "\n")
    relatorio.write("Nr. Usuário            Espaço utilizado     % do uso\n")
    for i, (nome, espaco) in enumerate(usuarios, start=1):
        percentual = calcular_percentual(espaco, espaco_total)
        relatorio.write(f"{i:<2} {nome:<20} {bytes_para_mb(espaco):>14.2f} MB {percentual:>12.2f}%\n")
    relatorio.write(f"\nEspaço total ocupado: {bytes_para_mb(espaco_total):.2f} MB\n")
    relatorio.write(f"Espaço médio ocupado: {bytes_para_mb(espaco_total / len(usuarios)):.2f} MB\n")
