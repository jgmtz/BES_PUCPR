'''Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.'''
nums= [] 
multiplicacao = 1
for num in range(5):
    num = int(input('digite um numero'))
    nums.append(num)
    multiplicacao *= num
soma = sum(nums)

print(nums)
print(multiplicacao)
print(soma)