votos = [0] * 7
opcoes = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
print("Enquete: Qual o melhor Sistema Operacional para uso em servidores?")
print("1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro\n0- Encerrar votação")
while True:
    voto = int(input("Informe o número correspondente ao Sistema Operacional (0 a 6): "))
    if voto == 0:
        break
    elif 1 <= voto <= 6:
        votos[voto] += 1
    else:
        print("Valor inválido. Por favor, informe um número de 0 a 6.")
total_votos = sum(votos)
print("\nResultado da enquete:")
print("Sistema Operacional   Votos   %")
print("-------------------  -----  ---")
for i in range(1, len(votos)):
    percentual = (votos[i] / total_votos) * 100 if total_votos > 0 else 0
    print(f"{opcoes[i-1]:<20} {votos[i]:>6}  {percentual:.1f}%")
print("-------------------  -----  ---")
print(f"Total                {total_votos}")
mais_votado = votos.index(max(votos))
percentual_mais_votado = (votos[mais_votado] / total_votos) * 100 if total_votos > 0 else 0
print(f"\nO Sistema Operacional mais votado foi o {opcoes[mais_votado-1]}, com {votos[mais_votado]} votos, "
      f"correspondendo a {percentual_mais_votado:.1f}% dos votos.")
