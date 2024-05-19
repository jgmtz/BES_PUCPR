'''Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
Imprima a idade e a altura na ordem inversa a ordem lida'''
idades = []
alturas = []
for i in range(5):
    idade =int(input(f'insira sua idade pessoa {i+1}: '))
    altura = int(input(f'insira sua altura pessoa {i+1}: '))
    idades.append(idade)
    alturas.append(altura)
alturas.reverse()
idades.reverse()
print(idades)
print(alturas)
    