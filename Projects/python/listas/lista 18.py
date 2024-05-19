NUM_JOGADORES = 23
votos = {jogador: 0 for jogador in range(1, NUM_JOGADORES + 1)}
total_votos = 0
print("Enquete: Quem foi o melhor jogador?")
while True:
    numero_jogador = int(input("Número do jogador (0=fim): "))
    if numero_jogador == 0:
        break
    elif 1 <= numero_jogador <= NUM_JOGADORES:
        votos[numero_jogador] += 1
        total_votos += 1
    else:
        print("Informe um valor entre 1 e 23 ou 0 para sair!")
print("\nResultado da votação:")
print(f"Foram computados {total_votos} votos.")
print("Jogador   Votos   %")
for jogador, voto in votos.items():
    if voto > 0:
        percentual = (voto / total_votos) * 100 if total_votos > 0 else 0
        print(f"{jogador:6} {voto:8} {percentual:.1f}%")
melhor_jogador = max(votos, key=votos.get)
percentual_melhor_jogador = (votos[melhor_jogador] / total_votos) * 100 if total_votos > 0 else 0
print(f"\nO melhor jogador foi o número {melhor_jogador}, com {votos[melhor_jogador]} votos, correspondendo a "
      f"{percentual_melhor_jogador:.1f}% do total de votos.")
arquivo = open("resultado_votacao.txt", "w")
arquivo.write("Resultado da votação:\n")
arquivo.write(f"Foram computados {total_votos} votos.\n")
arquivo.write("Jogador   Votos   %\n")
for jogador, voto in votos.items():
    if voto > 0:
        percentual = (voto / total_votos) * 100 if total_votos > 0 else 0
        arquivo.write(f"{jogador:6} {voto:8} {percentual:.1f}%\n")
arquivo.write(f"\nO melhor jogador foi o número {melhor_jogador}, com {votos[melhor_jogador]} votos, "
              f"correspondendo a {percentual_melhor_jogador:.1f}% do total de votos.")
