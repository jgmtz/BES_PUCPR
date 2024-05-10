'''Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa'''
lista = []
for i in range(10):
    num = int(input(f'insira o {i+1}° numero: '))
    lista.append(num)
lista.reverse()
print(lista)