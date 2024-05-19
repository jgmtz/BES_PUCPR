semente = 1234567
primeira_jogada = ((semente * 16807) % 2147483647) % 6 + 1
if primeira_jogada in [7, 11]:
    print("Natural! Você ganhou!")
elif primeira_jogada in [2, 3, 12]:
    print("Craps! Você perdeu!")
else:
    ponto = primeira_jogada
    print(f"Ponto: {ponto}")
while ponto != 0:
    semente = (semente * 16807) % 2147483647
    resultado = semente % 6 + 1
    if resultado == 7:
        print("Você tirou 7. Você perdeu!")
        break
    elif resultado == ponto:
        print("Você tirou o ponto novamente. Você ganhou!")
        break