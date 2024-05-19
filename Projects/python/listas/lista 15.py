
notas = []
while True:
    nota = float(input("Digite uma nota (-1 para encerrar): "))
    if nota == -1:
        break
    notas.append(nota)
quantidade = len(notas)
print(f"\nQuantidade de valores lidos: {quantidade}")
print("Valores na ordem informada:", ' '.join(map(str, notas)))
print("Valores na ordem inversa:")
for nota in reversed(notas):
    print(nota)
soma = sum(notas)
print(f"Soma dos valores: {soma}")
if quantidade > 0:
    media = soma / quantidade
    print(f"Média dos valores: {media:.2f}")
else:
    media = 0
    print("Média dos valores: N/A")
acima_da_media = sum(1 for nota in notas if nota > media)
print(f"Quantidade de valores acima da média: {acima_da_media}")
abaixo_de_sete = sum(1 for nota in notas if nota < 7)
print(f"Quantidade de valores abaixo de sete: {abaixo_de_sete}")
print("Programa encerrado. Obrigado!")
