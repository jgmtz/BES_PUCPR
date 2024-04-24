'''
Criar um programa que efetua a soma de duas matrizes 3x3, sabendo
que a soma das matrizes 3x3 é uma nova matriz 3x3 onde cada elemento
é resultado da soma dos elementos das matrizes na mesma posição.
'''
matriz1 = [[0,0,0],[0,0,0],[0,0,0]]
matriz2 = [[0,0,0],[0,0,0],[0,0,0]]
matriz3 = [[],[],[]]
for i in range(3): 
    for j in range(3):
        matriz1[i][j] = int(input(f'digite um valor para o termo [{i}][{j}] da matriz 1: '))
        matriz2[i][j] = int(input(f'digite um valor para o termo [{i}][{j}] da matriz 2: '))
        soma = matriz1[i][j] + matriz2[i][j]
        matriz3[i].append(soma) 
print('matriz 1: ') 
for i in range(3):
    print(matriz1[i])
print('matriz 2: ')
for i in range(3):
    print(matriz2[i])
print('a soma das matrizes é: ')
for i in range(3):
    print(matriz3[i])
