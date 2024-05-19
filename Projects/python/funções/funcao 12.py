palavra = input("Digite uma palavra: ")
palavra = palavra.lower()
caracteres = list(palavra)
tamanho = len(caracteres)
semente = 123456
for i in range(tamanho):
    j = (i * 2 + 1) * semente % tamanho
    caracteres[i], caracteres[j] = caracteres[j], caracteres[i]
palavra_embaralhada = ''.join(caracteres)
print("Palavra embaralhada:", palavra_embaralhada)
