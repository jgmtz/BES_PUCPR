'''Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as
consoantes'''
vogais = ['a','e','i','o','u']
consoantes = []
for i in range(10):
    caracteres = input(f'insira o {i+1}° caracter: ')
    if caracteres in vogais:
        consoantes.append(caracteres)
conso = len(consoantes)
print(consoantes)
print(conso)
if conso == True:
    
        