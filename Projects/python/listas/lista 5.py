'''Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor
PAR e os números IMPARES no vetor impar. Imprima os três vetores.'''
lista = []
pares = []
impares = []
for i in range(20):
    num = int(input(f'insira o {i+1}° nunero: '))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(lista)
print(pares)
print(impares)