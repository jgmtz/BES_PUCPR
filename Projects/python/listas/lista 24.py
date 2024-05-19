contadores = [0, 0, 0, 0, 0, 0]
semente = 1234567
for _ in range(100):
    semente = (semente * 16807) % 2147483647
    resultado = semente % 6 + 1
    contadores[resultado - 1] += 1
print("Resultados do lançamento de dados:")
for i in range(6):
    print(f"O número {i+1} foi obtido {contadores[i]} vezes.")
