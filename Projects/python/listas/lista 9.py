'''Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos
elementos do vetor'''
numeros = []
for i in range(10):
    nums = int(input('insira um numero: '))
    pow = nums ** 2
    numeros.append(pow)
soma = sum(numeros)
print(soma)
    
    