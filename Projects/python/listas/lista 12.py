'''Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de
13 anos possuem altura inferior à média de altura desses alunos'''
idades = []
alturas = []
inferior = []
for i in range(30):
    idade = int(input(f'insira a idade do aluno {i+1}: '))
    altura = int(input(f'insiea a altura do aluno {i+1}: '))
    idade += idade
    idades.append(idade)
    alturas.append(altura)
media = altura/2
if idade > 13 and altura < media:
    inferior.append(idade)
print(media)
print(len(inferior))