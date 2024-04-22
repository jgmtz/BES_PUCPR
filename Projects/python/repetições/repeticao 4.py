primeiro_numero = float(input("Digite o primeiro número: "))
menor = maior = primeiro_numero
for i in range(4):
    numero = float(input("Digite o próximo número: "))
    if numero < menor:
        menor = numero
    if numero > maior:
        maior = numero
print(f'Menor número: {menor}')
print(f'Maior número: {maior}')