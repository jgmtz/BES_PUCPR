'''Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0.'''
lista = []
for i in range(10):
    for j in range(4):
        num = int(input(f'insira a {j+1}° nota do {i+1}° aluno: ')) 
        lista.append(num)
    lista.clear()
    
    