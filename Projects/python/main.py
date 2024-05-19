lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9]
lista2.append(10)
print(lista2)
lista1.extend(lista2)
print(lista1)
lista1.insert(10, [3])
print(lista1)