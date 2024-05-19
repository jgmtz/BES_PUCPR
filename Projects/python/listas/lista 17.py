while True:
    nome_atleta = input("Nome do atleta: ")
    if not nome_atleta:
        break
    saltos = [] 
    for i in range(5):
        salto = float(input(f"{i + 1}º Salto: "))
        saltos.append(salto)
    media_saltos = sum(saltos) / 5
    print("\nResultado final:")
    print(f"Atleta: {nome_atleta}")
    print(f"Saltos: {' - '.join(map(str, saltos))} m")
    print(f"Média dos saltos: {media_saltos:.1f} m\n")