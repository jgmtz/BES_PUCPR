'''Faça um Programa que leia 4 notas, mostre as notas e a média na tela.'''
lista = []
for i in range(4):
    num = int(input(f'insira o {i + 1}° numero: '))
    lista.append(num)
print(lista)
media = sum(lista)/len(lista)
print(media)
