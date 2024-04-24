'''
Criar um programa que solicite ao usuário 2 listas com 5
elementos cada. Como resultado, criar uma terceira lista que
intercala os elementos das duas listas.
'''
lista1 = []
lista2 = []
lista3 = []
for i in range(5):
    elem = input(f'digite o {i + 1}° elemento da lista 1: ')
    lista1.append(elem)
for i in range(5):
    elem = input(f'digite o {i + 1}° elemento da lista 1: ')
    lista2.append(elem)
for i in range(5):
    lista3.append(lista1[i])
    lista3.append(lista2[i])
print(lista3)